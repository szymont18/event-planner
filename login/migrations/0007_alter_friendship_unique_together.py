# Generated by Django 4.2.10 on 2024-02-07 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_websiteuser_friends_friendship'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together={('from_user', 'to_user')},
        ),
    ]