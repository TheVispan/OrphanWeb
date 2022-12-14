# Generated by Django 4.1.2 on 2022-11-08 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_orphans_deduction_orphans_disable_and_more'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='orphans',
            name='deduction',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orphans',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orphans',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.gender'),
        ),
        migrations.AlterField(
            model_name='orphans',
            name='orphan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orphans',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.groups'),
        ),
    ]
