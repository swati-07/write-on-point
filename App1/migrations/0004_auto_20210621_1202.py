# Generated by Django 2.2 on 2021-06-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_blog_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='caption',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='photo1',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='photo2',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
