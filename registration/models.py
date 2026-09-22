from django.db import models
import uuid


class RegisteredPerson(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Other', 'Other'),
    ]

    # Registration ID
    registration_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    # Personal Information
    full_name = models.CharField(max_length=150)

    father_name = models.CharField(max_length=150)

    mother_name = models.CharField(
        max_length=150,
        blank=True
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES
    )

    # Contact Information
    mobile = models.CharField(max_length=15)

    alternate_mobile = models.CharField(
        max_length=15,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    # Community Information
    gotra = models.CharField(
        max_length=100,
        blank=True
    )

    pur = models.CharField(
        max_length=150,
        blank=True
    )

    native_place = models.CharField(
        max_length=150,
        blank=True
    )

    # Address
    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    district = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    pincode = models.CharField(
        max_length=10
    )

    # Professional Information
    occupation = models.CharField(
        max_length=150,
        blank=True
    )

    education = models.CharField(
        max_length=150,
        blank=True
    )

    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS_CHOICES,
        blank=True
    )

    # Registration timestamp
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name