# Generated by Django 4.1.5 on 2023-01-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_venue_washroom_venues_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='status',
            field=models.CharField(blank=True, choices=[('ONLINE', 'Online'), ('OFFLINE', 'Offline')], default='OFFLINE', max_length=50, null=True),
        ),
    ]
