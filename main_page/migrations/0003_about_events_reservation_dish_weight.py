# Generated by Django 4.1.5 on 2023-02-07 12:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_alter_category_options_alter_dish_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('video', models.URLField(help_text='https://www.youtube.com/watch?v=f6AOLJNPorY&ab_channel=TretyakovProduction')),
                ('photo', models.ImageField(blank=True, upload_to='promo/%Y-%m-%d')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('date', models.DateTimeField(help_text='Enter date and time of event')),
                ('is_visible', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, upload_to='events/%Y-%m-%d')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='', regex='')])),
                ('persons', models.SmallIntegerField()),
                ('message', models.TextField(blank=True, max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_processing', models.DateField(auto_now=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.AddField(
            model_name='dish',
            name='weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
