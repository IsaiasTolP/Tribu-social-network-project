# Generated by Django 5.1.2 on 2024-11-08 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waves', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wave',
            options={'ordering': ['-created_at']},
        ),
    ]