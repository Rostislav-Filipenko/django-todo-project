# Generated by Django 5.1.7 on 2025-04-02 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_todoitem_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
