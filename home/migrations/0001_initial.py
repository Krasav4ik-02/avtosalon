# Generated by Django 3.2.19 on 2023-11-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=30, verbose_name='Марка машины')),
                ('car_image', models.ImageField(upload_to='')),
            ],
        ),
    ]