# Generated by Django 2.2.3 on 2019-08-23 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_userprofile_input'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='Input',
        ),
    ]
