from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(max_length=254, unique=True)
  name = models.CharField(max_length=254, null=False, blank=False)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  last_login = models.DateTimeField(null=True, blank=True)
  date_joined = models.DateTimeField(auto_now_add=True)

  #enumerations used
  BRANCH_CHOICES = (
    ('APD', 'Architecture, Planning and Design'),
    ('CER', 'Ceramic Engineering and Technology'),
    ('CHE', 'Chemical Engineering'),
    ('CIV', 'Civil Engineering'),
    ('CSE', 'Computer Science and Engineering'),
    ('EEE', 'Electrical Engineering'),
    ('ECE', 'Electronics Engineering'),
    ('MEC', 'Mechanical Engineering'),
    ('MET', 'Metallurgical Engineering'),
    ('MIN', 'Mining Engineering'),
    ('PHE', 'Pharmaceutical Engineering and Technology'),
    ('IC', 'Chemistry'),
    ('MAT', 'Mathematical Sciences'),
    ('EP', 'Physics'),
    ('BCE', 'Biochemical Engineering'),
    ('BME', 'Biomedical Engineering'),
    ('SMST', 'Materials Science and Technology'),
  )
  
  DEGREE_CHOICES = (
    ('Btech', 'B. Tech.'),
    ('Mtech', 'M. Tech.'),
    ('IDD', 'IDD'),
  )

  ROLE_CHOICES = (
    ('STUDENT', 'Student'),
    ('TPR', 'TPR'),
    ('TPV', 'TPV'),
    ('CORE', 'Core'),
    ('DUTY', 'Duty'),
    ('VENUE', 'Venue'),
    ('SCHEDULING', 'Scheduling'),
    ('PORTAL', 'Portal'),
  )

  #fields
  roll_number = models.CharField(
    max_length=8,         # Enforces 8 characters length
    unique=True,          # Ensures uniqueness
    primary_key=True,     # Marks it as a primary key
    null=False,           # Does not allow null values
    blank=False,          # Requires a value in forms
    validators=[
        RegexValidator(
            regex=r'^\d{8}$',   # Enforces 8 digits with regex
            message="Roll number must be exactly 8 digits."
        ),
    ],
    error_messages={
        'unique': 'This roll number already exists.',
        'blank': 'Roll number cannot be empty.',
        'null': 'Roll number cannot be empty.',
    }
  )

  phone_number = models.CharField(
    max_length=10,  # Set the max length to 10
    unique=True,    # Ensures uniqueness
    null=False,     # Does not allow null values
    validators=[
      RegexValidator(
          regex=r'^\d{10}$',  # Enforces exactly 10 digits with regex
          message="Phone number must be exactly 10 digits."
      ),
    ],
    error_messages={
      'unique': 'This phone number is already in use.',
      'null': 'Phone number cannot be null.',
      'blank': 'Phone number cannot be empty.',
    }
  )

  branch = models.CharField(
    max_length=32,     # Set the max length to 3 characters (e.g., 'APD')
    choices=BRANCH_CHOICES,
    null=False,       # Does not allow null values
    blank=False,      # Requires a value in forms
  )
  
  degree = models.CharField(
    max_length=5,     # Set the max length to accommodate the longest choice
    choices=DEGREE_CHOICES,
    null=False,       # Does not allow null values
    blank=False,      # Requires a value in forms
  )
  
  role = models.CharField(
    max_length=10,   # Set the max length to accommodate the longest choice
    choices=ROLE_CHOICES,
    null=False,       # Does not allow null values
    default='STUDENT',  # Set the default value to 'STUDENT'
    blank=False,      # Requires a value in forms
  )
  
  USERNAME_FIELD = 'email'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()

  def __str__(self):
    return 'rno : {self.roll_number} name : {self.name} email : {self.email} branch : {self.branch} degree : {self.degree} role : {self.role}'