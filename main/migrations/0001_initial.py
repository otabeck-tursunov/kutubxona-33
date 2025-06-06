# Generated by Django 5.2 on 2025-04-24 11:03

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kutubxonachi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('ish_vaqti', models.CharField(choices=[('08:00-12:30', '08:00-12:30'), ('12:30-18:00', '12:30-18:00'), ('18:00-00:00', '18:00-00:00')], default='08:00-12:30', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=20)),
                ('t_sana', models.DateField(blank=True, null=True)),
                ('kitob_soni', models.PositiveSmallIntegerField(null=True)),
                ('tirik', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('guruh', models.CharField(max_length=50)),
                ('kurs', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('kitob_soni', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('janr', models.CharField(max_length=50)),
                ('sahifa', models.PositiveSmallIntegerField()),
                ('muallif', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.muallif')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olingan_sana', models.DateField(auto_now_add=True)),
                ('qaytargan_sana', models.DateField(blank=True, null=True)),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kitob')),
                ('kutubxonachi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.kutubxonachi')),
                ('talaba', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.talaba')),
            ],
        ),
    ]
