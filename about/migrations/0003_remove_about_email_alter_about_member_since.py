# Generated by Django 4.2.11 on 2024-07-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='email',
        ),
        migrations.AlterField(
            model_name='about',
            name='member_since',
            field=models.DateTimeField(),
        ),
    ]