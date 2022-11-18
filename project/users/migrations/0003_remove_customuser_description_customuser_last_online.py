# Generated by Django 4.1.3 on 2022-11-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_age_customuser_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='description',
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_online',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
