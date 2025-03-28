# Generated by Django 5.1.7 on 2025-03-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitem',
            options={'ordering': ('id',), 'verbose_name': 'ToDo Item'},
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
