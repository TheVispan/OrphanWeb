# Generated by Django 4.1.2 on 2022-11-07 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_orphans_dateofbirth_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gendername', models.CharField(max_length=4)),
            ],
        ),
        migrations.AlterField(
            model_name='orphans',
            name='dateofbirth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='orphans',
            name='dateofdeduction',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='orphans',
            name='dateofreceipt',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='orphans',
            name='number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='orphans',
            name='orphan',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='orphans',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.gender'),
        ),
    ]
