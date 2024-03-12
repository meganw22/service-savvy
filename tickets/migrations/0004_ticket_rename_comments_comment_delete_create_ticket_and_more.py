# Generated by Django 4.2.11 on 2024-03-12 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0003_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('job_category', models.IntegerField(choices=[(0, 'Choose Type'), (1, 'Plumbing'), (2, 'Lighting'), (3, 'Heating'), (4, 'Cleaning'), (5, 'Vending Services'), (6, 'Air Conditioning'), (7, 'Waste'), (8, 'Other')], default=0)),
                ('job_description', models.CharField(max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=200)),
                ('priority', models.IntegerField(choices=[(0, 'Priority Level'), (1, 'High (<2 hours)'), (2, 'Medium (<1 day)'), (3, 'Low (1 day +)')], default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tickets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
        migrations.RenameModel(
            old_name='comments',
            new_name='Comment',
        ),
        migrations.DeleteModel(
            name='create_ticket',
        ),
        migrations.AlterField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tickets.ticket'),
        ),
    ]
