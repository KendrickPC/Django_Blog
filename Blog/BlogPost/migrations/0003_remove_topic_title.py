# Generated by Django 2.1.4 on 2019-01-03 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPost', '0002_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='title',
        ),
    ]
