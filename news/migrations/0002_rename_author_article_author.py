# Generated by Django 3.2.4 on 2021-07-20 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Author',
            new_name='author',
        ),
    ]
