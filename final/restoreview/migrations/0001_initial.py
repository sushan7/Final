# Generated by Django 2.1.7 on 2019-04-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restoinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resto_name', models.CharField(max_length=200)),
                ('resto_review', models.CharField(max_length=3)),
                ('resto_type', models.CharField(max_length=50)),
            ],
        ),
    ]
