# Generated by Django 4.1.3 on 2022-11-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_orphans_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orphans',
            name='number',
        ),
        migrations.AlterField(
            model_name='orphans',
            name='diagnostics',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='orphans',
            name='featuresdiagnostics',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='orphans',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orphans',
            name='riskgroup',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]