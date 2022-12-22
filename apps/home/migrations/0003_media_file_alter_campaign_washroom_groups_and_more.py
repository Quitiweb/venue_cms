# Generated by Django 4.1.3 on 2022-12-22 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='washroom_groups',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='home.washroom'),
        ),
        migrations.AlterField(
            model_name='media',
            name='size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='washroom',
            name='faucets',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='washrooms', to='home.faucet'),
        ),
    ]