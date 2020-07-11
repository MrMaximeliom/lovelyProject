# Generated by Django 3.0.6 on 2020-06-12 14:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabet characters are allowed.')], verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabet characters are allowed.')], verbose_name='last name'),
        ),
    ]
