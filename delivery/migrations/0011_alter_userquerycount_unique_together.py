# Generated by Django 5.1 on 2024-11-12 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0010_alter_userquerycount_query_count_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userquerycount',
            unique_together=set(),
        ),
    ]
