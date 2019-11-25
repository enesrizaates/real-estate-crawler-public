# Generated by Django 2.2.5 on 2019-10-16 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sahibinden', '0011_auto_20191016_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_url', models.CharField(blank=True, max_length=256, null=True)),
                ('web_url', models.CharField(blank=True, max_length=256, null=True)),
                ('picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sahibinden.Post')),
            ],
        ),
    ]