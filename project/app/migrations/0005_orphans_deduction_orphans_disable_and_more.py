# Generated by Django 4.1.2 on 2022-11-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_gender_alter_orphans_dateofbirth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orphans',
            name='deduction',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='orphans',
            name='disable',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='orphans',
            name='orphan',
            field=models.BooleanField(null=True),
        ),
    ]
