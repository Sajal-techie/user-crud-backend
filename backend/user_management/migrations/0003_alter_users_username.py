# Generated by Django 5.0.4 on 2024-04-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_users_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
