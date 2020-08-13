# Generated by Django 2.2.12 on 2020-08-13 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_client_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=19, verbose_name='Price of cameo'),
        ),
    ]
