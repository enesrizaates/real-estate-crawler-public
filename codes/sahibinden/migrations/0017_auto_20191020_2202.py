# Generated by Django 2.2.5 on 2019-10-20 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sahibinden', '0016_auto_20191020_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
    ]