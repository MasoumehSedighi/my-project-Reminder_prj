# Generated by Django 3.2.5 on 2021-07-28 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categories_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['categories_name'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.categories')),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
    ]
