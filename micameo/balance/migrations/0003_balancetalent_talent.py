# Generated by Django 2.2.15 on 2020-11-01 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('balance', '0002_balancetalentdetail_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='balancetalent',
            name='talent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Talent'),
        ),
    ]