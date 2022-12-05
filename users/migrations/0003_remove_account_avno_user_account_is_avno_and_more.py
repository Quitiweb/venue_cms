# Generated by Django 4.1.3 on 2022-12-05 15:56

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_account_avno_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='avno_user',
        ),
        migrations.AddField(
            model_name='account',
            name='is_avno',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as an AVNO user.', verbose_name='avno user'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, help_text='+34999999999', max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Format: '+999999999'. Max 15 digits.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avno_user', models.CharField(default='', max_length=50)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.account',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
