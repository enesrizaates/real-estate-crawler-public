# Generated by Django 2.2.5 on 2019-10-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahibinden', '0005_properties_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='descriptions',
            field=models.CharField(blank=True, max_length=1440, null=True),
        ),
    ]
