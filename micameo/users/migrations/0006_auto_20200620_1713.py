# Generated by Django 2.2.12 on 2020-06-20 22:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200613_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('sub_name', models.CharField(error_messages={'unique': 'A category with that name already exist'}, max_length=30, unique=True, verbose_name='Sub category')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='talent',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='talent_category', to='users.SubCategory'),
        ),
    ]
