# Generated by Django 2.2.5 on 2019-10-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahibinden', '0014_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
