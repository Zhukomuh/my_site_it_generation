# Generated by Django 4.1.5 on 2023-02-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0007_chefs_whyus'),
    ]

    operations = [
        migrations.AddField(
            model_name='chefs',
            name='title',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
