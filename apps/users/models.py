from time import time

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


<<<<<<< HEAD
def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)


class User(models.Model):
    PRESIDENT = 'PR'
    VICEPRESIDENT = 'VP'
    TREASURER = 'TR'
    SECRETARY = 'SE'
    VOCAL = 'VO'
    MEMBER = 'ME'
    POSITION_OPTIONS = (
        (PRESIDENT, 'President'),
        (VICEPRESIDENT, 'Vice-President'),
        (TREASURER, 'Treasurer'),
        (SECRETARY, 'Secretary'),
        (VOCAL, 'Vocal'),
        (MEMBER, 'Member'),
    )
    MALE = 'M'
    FEMALE = 'F'
=======
class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, gender, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            gender=gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, gender, password):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
>>>>>>> e58e33420508ae641ecd4ea573d48289457b65ab
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
<<<<<<< HEAD
    student_number = models.CharField(max_length=9, unique=True)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              default='M')
=======
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
>>>>>>> e58e33420508ae641ecd4ea573d48289457b65ab
    active_member = models.BooleanField(default=False)
    amount_payed = models.FloatField(default=0)
    position = models.CharField(max_length=2, choices=POSITION_OPTIONS,
                                default='ME')
    picture = models.FileField(upload_to=get_upload_file_name)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
