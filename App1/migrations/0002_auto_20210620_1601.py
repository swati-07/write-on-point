# Generated by Django 2.2 on 2021-06-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
