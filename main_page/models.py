import uuid

from django.db import models
from django.core.validators import RegexValidator
from tinymce.models import HTMLField


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)


class Dish(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/%Y-%m-%d', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    weight = models.IntegerField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position',)


class About(models.Model):
    title = models.CharField(max_length=255, unique=True, db_index=True)
    description = HTMLField()
    video = models.URLField(help_text='enter url of video')
    photo = models.ImageField(upload_to='promo/%Y-%m-%d', blank=True)


class Events(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(help_text='Enter date and time of event')
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='events/%Y-%m-%d', blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('date',)


class Reservation(models.Model):
    phone_validator = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Error phone number')
    email_validator = RegexValidator(regex=r'[a-zA-Z0-9]*(-?\.?[_a-zA-Z0-9])*@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*',
                                     message='Error email')
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, validators=[phone_validator])
    email = models.CharField(max_length=50, validators=[email_validator])
    persons = models.SmallIntegerField()
    message = models.TextField(max_length=255, blank=True)

    date = models.DateField(auto_now_add=True)
    date_processing = models.DateField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.phone_number}'

    class Meta:
        ordering = (
            '-date',
        )


class PhotoGallery(models.Model):
    photo = models.ImageField(upload_to='our_photo/%Y-%m-%d', blank=True)
    is_visible = models.BooleanField(default=True)


class Chefs(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='chefs/%Y-%m-%d', blank=True)
    description = models.TextField(max_length=500, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = (
            'is_visible',
        )


class WhyUs(models.Model):
    title = models.CharField(max_length=50)
    position = models.SmallIntegerField()
    photo = models.ImageField(upload_to='why_us/%Y-%m-%d', blank=True)
    description = models.TextField(max_length=500, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = (
            'is_visible',
        )
