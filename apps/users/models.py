from time import time

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

from multiselectfield import MultiSelectField


def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,
                    student_number, gender, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            student_number=student_number,
            gender=gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name,
                         student_number, gender, password):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            student_number=student_number,
            gender=gender,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
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
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    BASIC_SPANISH_I = 'ESPA-3101'
    BASIC_SPANISH_II = 'ESPA-3102'
    TECHNICAL_REPORT_WRITING_SPANISH = 'ESCO-4005'
    BASIC_ENGLISH_I = 'INGL-3101'
    BASIC_ENGLISH_II = 'INGL-3102'
    TECHNICAL_REPORT_WRITING_ENGLISH = 'INCO-4025'
    PRE_CALCULUS_I = 'MATE-3171'
    PRE_CALCULUS_II = 'MATE-3172'
    DISCRETE_MATHEMATICS = 'MATE-3175'
    CALCULUS_I = 'MATE-3031'
    CALCULUS_II = 'MATE-3032'
    STATISTICS_USING_COMPUTERS = 'MATE-3026'
    ALGORITHMS_AND_PROGRAM_DEVELOPMENT_I = 'COTI-3101'
    ALGORITHMS_AND_PROGRAM_DEVELOPMENT_II = 'COTI-3102'
    DATA_STRUCTURES = 'SICI-4036'
    WEB_APPLICATIONS = 'COTI-4210'
    DATABASE = 'SICI-4030'
    COURSES_CHOICES = (
        ('COTI-3101', 'Algorithms and Program Development I'),
        ('COTI-3102', 'Algorithms and Program Development II'),
        ('SICI-4036', 'Data Structures'),
        ('COTI-4210', 'Web Applications'),
        ('SICI-4030', 'Database'),
        ('MATE-3171', 'Pre-Calculus I'),
        ('MATE-3172', 'Pre-Calculus II'),
        ('MATE-3175', 'Discrete Mathematics'),
        ('MATE-3031', 'Calculus I'),
        ('MATE-3032', 'Calculus II'),
        ('MATE-3026', 'Statistics Using Computers'),
        ('ESPA-3101', 'Basic Spanish I'),
        ('ESPA-3102', 'Basic Spanish II'),
        ('ESCO-4005', 'Technical Report Writing In Spanish'),
        ('INGL-3101', 'Basic English I'),
        ('INGL-3102', 'Basic English II'),
        ('INCO-4025', 'Technical Report Writing In English'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    student_number = models.CharField(max_length=9, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    amount_payed = models.FloatField(default=0)
    position = models.CharField(max_length=2, choices=POSITION_OPTIONS,
                                default='ME')
    phone_number = models.CharField(max_length=10)
    courses = MultiSelectField(choices=COURSES_CHOICES)
    programming_languages = models.CharField(max_length=400)
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'student_number']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

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
