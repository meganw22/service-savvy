# Generated by Django 4.2.11 on 2024-03-29 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='ticket',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='completed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='completed_tickets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='job_category',
            field=models.IntegerField(choices=[(0, 'Plumbing'), (1, 'Lighting'), (2, 'Heating'), (3, 'Cleaning'), (4, 'Vending Services'), (5, 'Air Conditioning'), (6, 'Waste'), (7, 'Other')], default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.IntegerField(choices=[(0, 'High (<2 hours)'), (1, 'Medium (<1 day)'), (2, 'Low (1 day +)')], default=0),
        ),
    ]
