# Generated by Django 4.2.11 on 2024-03-09 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='create_ticket',
            options={'ordering': ['priority']},
        ),
    ]
