# Generated by Django 4.1.3 on 2022-12-23 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_nmae', models.CharField(max_length=100)),
                ('salary', models.IntegerField(default=0)),
                ('bonous', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('hire_date', models.DateField()),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.department')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.role')),
            ],
        ),
    ]