# Generated by Django 2.2.15 on 2020-11-01 15:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceMiCameo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('balance_name', models.CharField(default='Micameo', max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BalanceOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('balance_name', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BalanceTalent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BalanceTalentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('balance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balance.BalanceTalent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
