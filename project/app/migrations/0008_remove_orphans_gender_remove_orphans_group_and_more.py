# Generated by Django 4.1.3 on 2022-11-10 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_deduction_orphans_expelled_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orphans',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='orphans',
            name='group',
        ),
        migrations.DeleteModel(
            name='Relatives',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
        migrations.DeleteModel(
            name='orphans',
        ),
    ]
