from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, ("Male")),
        (GENDER_FEMALE, ("Female")),
        (GENDER_OTHER, ("Other")),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_SPANISH = "es"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, ("English")),
        (LANGUAGE_SPANISH, ("Spanish")),
    )

    CURRENCY_USD = "usd"
    CURRENCY_EURO = "euro"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_EURO, "EURO"))

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGING_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGING_KAKAO, "Kakao"),
    )

    first_name = models.CharField(
        ("first name"), max_length=30, blank=True, default="Unnamed User"
    )
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(
        ("gender"), choices=GENDER_CHOICES, max_length=10, blank=True
    )
    bio = models.TextField(("bio"), blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        ("language"),
        choices=LANGUAGE_CHOICES,
        max_length=2,
        blank=True,
        default=LANGUAGE_ENGLISH,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=4, blank=True, default=CURRENCY_EURO
    )
    superhost = models.BooleanField(default=False)
    