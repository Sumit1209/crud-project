# Generated by Django 4.1.3 on 2022-12-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='last_nmae',
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
    ]
