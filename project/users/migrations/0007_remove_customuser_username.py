# Generated by Django 4.1.3 on 2022-11-11 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
