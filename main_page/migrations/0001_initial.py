# Generated by Django 4.1.5 on 2023-01-28 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('position', models.SmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('position', models.SmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
                ('ingredients', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('is_special', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.category')),
            ],
        ),
    ]
