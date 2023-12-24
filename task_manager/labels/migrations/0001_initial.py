# Generated by Django 4.2.6 on 2023-12-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0002_alter_taskmodel_description_alter_taskmodel_executor'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('tasks', models.ManyToManyField(to='tasks.taskmodel')),
            ],
        ),
    ]
