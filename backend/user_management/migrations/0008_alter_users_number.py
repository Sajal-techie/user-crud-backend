# Generated by Django 5.0.4 on 2024-04-22 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0007_rename_customuser_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]