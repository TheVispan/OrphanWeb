# Generated by Django 4.1.3 on 2022-11-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orphans',
            name='icon',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
