# Generated by Django 3.2.5 on 2021-07-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrador',
            name='password',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
