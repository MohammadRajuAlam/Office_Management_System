# Generated by Django 5.0 on 2024-06-13 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0013_alter_bank_bank_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_type',
            field=models.CharField(choices=[('Goverment', 'Goverment'), ('Semi Goverment', 'Semi Goverment'), ('Private', 'Private'), ('Semi Private', 'Semi Private')], error_messages={'bank_type': 'Select correct given choice'}, max_length=30),
        ),
    ]
