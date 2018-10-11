# Generated by Django 2.1.2 on 2018-10-11 05:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statusmu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=300)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
