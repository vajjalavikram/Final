# Generated by Django 2.2.3 on 2019-08-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20190817_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone',
            new_name='Name_1',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Name_2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]