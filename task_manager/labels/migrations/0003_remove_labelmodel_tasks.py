# Generated by Django 4.2.6 on 2023-12-24 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_labelmodel_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labelmodel',
            name='tasks',
        ),
    ]
