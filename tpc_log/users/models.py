from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    A User class extending AbstractUser
    """
    username = None
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    #enumerations used in the model
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
    name = models.CharField(max_length=100, blank=False, null=False)

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
    
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email