# Generated by Django 4.1.3 on 2022-11-12 16:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('media_file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Faucet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mac', models.CharField(max_length=100)),
                ('ip_address', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('playlist', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=50)),
                ('size', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=150)),
                ('address2', models.CharField(blank=True, max_length=150, null=True)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('playlist', models.CharField(blank=True, max_length=100, null=True)),
                ('ad_approver', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Format: '+999999999'. Max 15 digits.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('contract_start', models.DateField(blank=True, null=True)),
                ('contract_end', models.DateField(blank=True, null=True)),
                ('loop_size', models.IntegerField(default=0)),
                ('max_ad_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Washroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('group_association', models.CharField(max_length=50)),
                ('faucets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.faucet')),
            ],
        ),
    ]