# Generated by Django 3.2.7 on 2021-09-25 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='little',
            new_name='title',
        ),
    ]
