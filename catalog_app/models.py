from django.db import models
from members_app.models import User
# Create your models here.


class Category(models.Model):

    GENDER_CHOICES = [
        ("N", "NARRATIVE"),
        ("T", "TERROR"),
        ("H", "HUMOR"),
        ("R", "ROMANTIC"),
    ]

    EDITION_CHOICES = [
        ("FD", "FIRST EDITION"),
        ("SD", "SECOND EDITION"),
        ("TD", "THIRD EDITION"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=1
    )
    edition = models.CharField(
        choices=EDITION_CHOICES, max_length=2
    )

    cover = models.CharField(max_length=25)
    color = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.cover} | {self.gender} | {self.owner.email}"
