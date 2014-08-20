from time import time
from datetime import datetime

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.mail import send_mail

from multiselectfield import MultiSelectField
from autoslug import AutoSlugField

from .constants import POSITION_OPTIONS, GENDER_CHOICES, COURSES_CHOICES
from .constants import PROG_LANGUAGES_AND_FRAMEWORKS


def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)


def populate_user_slug(instance):
    return instance.get_full_name()


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,
                    student_number, gender, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            student_number=student_number,
            gender=gender,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name,
                         student_number, gender, password, phone_number):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            student_number=student_number,
            gender=gender,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    student_number = models.CharField(max_length=9, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    amount_payed = models.FloatField(default=0)
    position = models.CharField(max_length=2, choices=POSITION_OPTIONS,
                                default='ME')
    phone_number = models.CharField(max_length=10, blank=True)
    courses = MultiSelectField(choices=COURSES_CHOICES, blank=True)
    programming_languages = MultiSelectField(
        choices=PROG_LANGUAGES_AND_FRAMEWORKS,
        blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from=populate_user_slug, unique=True)

    amount_registered = None

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'gender', 'student_number', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.amount_registered = self.amount_payed

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        fullname = '%s %s' % (self.first_name, self.last_name)
        return fullname

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def get_student_number(self):
        return self.student_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


def check_payed_amount(sender, **kwargs):
    c = kwargs['instance']
    date_info = datetime.now()

    if c.amount_registered != c.amount_payed:
        if c.amount_payed != 0 and c.amount_payed >= 15:
            full_payment_receipt = (
                'Nombre: ' + c.first_name.capitalize() + ' '
                + c.last_name.capitalize()
                + '\nFecha y hora: ' +
                date_info.strftime("%Y-%m-%d %H:%M")
                + '\nCantidad pagada: $' +
                str(c. amount_payed)
                + '\nCantidad a pagar: $' + str(0)
                + '\n\nSite: aecc-uprb.herokuapp.com')
            send_mail(
                'AECC Recibo', full_payment_receipt, 'example@example.com',
                [c.email], fail_silently=False)

        elif c.amount_payed < 15 and c.amount_payed != 0:
            amount_owed = 15 - c.amount_payed
            partial_payment_receipt = (
                'Nombre: ' + c.first_name.capitalize()
                + ' ' + c.last_name.capitalize()
                + '\nFecha y hora: ' + date_info.strftime("%Y-%m-%d %H:%M")
                + '\nCantidad pagada: $' + str(c. amount_payed)
                + '\nCantidad a pagar: $' + str(amount_owed)
                + '\n\nSite: aecc-uprb.herokuapp.com')
            send_mail('AECC Recibo', partial_payment_receipt,
                      'example@example.com', [c.email], fail_silently=False)
    c.amount_registered = c.amount_payed


post_save.connect(check_payed_amount, sender=User)
