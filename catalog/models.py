from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings

class LiteraryFormat(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("name",)


class Author(AbstractUser):
    pseudonym = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        ordering = ("username",)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    format = models.ForeignKey(
        LiteraryFormat,
        on_delete=models.CASCADE,
        related_name="books"
    )
    authors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="books"
    )

    def __str__(self):
        return f"{self.title} (price: {self.price})"

    class Meta:
        ordering = ("title",)