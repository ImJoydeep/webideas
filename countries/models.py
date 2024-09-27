from django.db import models

class Country(models.Model):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )

    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    country_flag = models.ImageField(upload_to='flags/')
    country_archive = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='A')

    def __str__(self):
        return self.country_name

class City(models.Model):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )

    city_name = models.CharField(max_length=100)
    city_archive = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='A')

    def __str__(self):
        return self.city_name