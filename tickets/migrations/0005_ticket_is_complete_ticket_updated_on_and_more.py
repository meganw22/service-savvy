# Generated by Django 4.2.11 on 2024-03-12 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticket_rename_comments_comment_delete_create_ticket_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ticket',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='job_description',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='location',
            field=models.TextField(max_length=200),
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived_at', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket')),
            ],
        ),
    ]
