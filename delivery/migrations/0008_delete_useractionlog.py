# Generated by Django 5.1 on 2024-11-11 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_useractionlog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserActionLog',
        ),
    ]
