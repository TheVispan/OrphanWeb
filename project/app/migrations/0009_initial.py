# Generated by Django 4.1.3 on 2022-11-10 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0008_remove_orphans_gender_remove_orphans_group_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gendername', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Relatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('kinship', models.CharField(max_length=255)),
                ('phonenumbers', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('dateofbirth', models.DateField(null=True)),
                ('placeofbirth', models.CharField(max_length=255)),
                ('healthstatus', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Orphans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('dateofbirth', models.DateField(null=True)),
                ('placeofbirth', models.CharField(max_length=255)),
                ('orphan', models.BooleanField(default=False)),
                ('expelled', models.BooleanField(default=False)),
                ('disable', models.BooleanField(default=False)),
                ('dateofreceipt', models.DateField(null=True)),
                ('dateofdeduction', models.DateField(null=True)),
                ('diagnostics', models.CharField(max_length=255, null=True)),
                ('featuresdiagnostics', models.CharField(max_length=255, null=True)),
                ('riskgroup', models.CharField(max_length=255, null=True)),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.gender')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.groups')),
            ],
        ),
    ]
