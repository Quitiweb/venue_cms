# Generated by Django 4.1.5 on 2023-02-06 15:29

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_useradmin_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
