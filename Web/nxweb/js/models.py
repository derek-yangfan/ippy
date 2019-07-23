from django.db import models
from django.urls import reverse

# Create your models here.


class Country(models.Model):

    name = models.CharField(verbose_name="country", max_length=50)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(verbose_name="city", max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="country",)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(verbose_name="client", max_length=50)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name="country")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name="city")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dropdown:client_detail', kwargs={'pk': self.pk})
