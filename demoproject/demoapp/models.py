from django.db import models


# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender_choices=(('male','Male'),('female','Female'),)
    gender=models.CharField(max_length=10,choices=gender_choices,null=True)
    email =models.CharField(max_length=100)
    phone =models.IntegerField(max_length=50)
    address=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    hobbies=models.CharField(max_length=50,blank=True)
    COUNTRY_CHOICES = [
        ('India', 'India'),
        ('USA', 'USA'),
    ]

    CITY_CHOICES = [
        ('Kerala', 'Kerala'),
        ('TamilNadu', 'TamilNadu'),
        ('Mexico', 'Mexico'),
        ('Chicago', 'Chicago'),
    ]

    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, blank=True)
    city = models.CharField(max_length=50, choices=CITY_CHOICES, blank=True)

    def __str__(self):
        return f'{self.country} - {self.city}'

    def __str__(self):
        return self.first_name


