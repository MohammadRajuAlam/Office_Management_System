# Generated by Django 5.0 on 2024-06-13 11:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0007_alter_bank_bank_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_id',
            field=models.CharField(error_messages={'error': 'HAAAGiven bank_id is already used.'}, max_length=10, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_bank_id', message='Bank ID must contain both characters and numbers.', regex='^(?=.*[a-zA-Z])(?=.*\\d)[a-zA-Z\\d]*$')]),
        ),
    ]
