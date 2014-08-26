from time import time
from datetime import datetime

from django.db import models
from django.conf import settings
from django.db.models import Q
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

from multiselectfield import MultiSelectField
from autoslug import AutoSlugField

from .constants import POSITION_OPTIONS, GENDER_CHOICES, COURSES_CHOICES
from .constants import PROG_LANGUAGES_AND_FRAMEWORKS, YEARS_PAYED


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

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'gender', 'student_number', 'phone_number']

    def __unicode__(self):
        return self.email

    def has_valid_membership(self):
        date_info = datetime.now()
        payments = self.payment_set.filter(Q(year_payed=date_info.year) | Q(year_payed=date_info.year-1))
        if payments.count() >= 1:
            for p in payments:
                if p.amount_payed == settings.AECC_UPRB_MEMBER_FEE \
                        and (datetime.strptime("6/1/"+p.year_payed, "%m/%d/%Y") \
                             <= p.created_at.replace(tzinfo=None) \
                             <= datetime.strptime("6/1/"+str(int(p.year_payed)+1), "%m/%d/%Y")):
                    return True
        return False

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


class Payment(models.Model):
    class Meta:
        unique_together = ('payed_by', 'year_payed')

    payed_by = models.ForeignKey(User)
    amount_payed = models.FloatField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(settings.AECC_UPRB_MEMBER_FEE)])
    year_payed = models.CharField(choices=YEARS_PAYED, max_length=6)
    created_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s - %s" % (self.payed_by, self.year_payed)


def validate_user_payment(sender, **kwargs):
    payment = kwargs['instance']
    date_info = datetime.now()

    if payment.amount_payed <= settings.AECC_UPRB_MEMBER_FEE and payment.amount_payed:
        receipt = (
            'Nombre: ' + payment.payed_by.first_name.capitalize() + ' '
            + payment.payed_by.last_name.capitalize()
            + '\nFecha y hora: ' + date_info.strftime("%Y-%m-%d %H:%M")
            + '\nCantidad pagada: $' + str(payment.amount_payed)
            + '\nCantidad a pagar: $' + str(settings.AECC_UPRB_MEMBER_FEE - payment.amount_payed)
            + '\n\nSite: aecc-uprb.herokuapp.com')
        send_mail(
            'AECC Recibo', receipt, 'example@example.com',
            [payment.payed_by.email], fail_silently=False)

post_save.connect(validate_user_payment, sender=Payment)
