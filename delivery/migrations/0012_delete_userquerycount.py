# Generated by Django 5.1 on 2024-11-12 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0011_alter_userquerycount_unique_together'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserQueryCount',
        ),
    ]
