# Generated by Django 3.2.5 on 2021-07-28 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-due_date']},
        ),
    ]
