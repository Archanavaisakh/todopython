# Generated by Django 4.1.2 on 2022-12-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttddapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-10-28'),
            preserve_default=False,
        ),
    ]
