# Generated by Django 2.2.12 on 2020-06-14 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200613_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='talent_category', to='users.Category'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='description',
            field=models.TextField(blank=True, max_length=600, verbose_name='Your Description'),
        ),
    ]
