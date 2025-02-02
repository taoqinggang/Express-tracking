# Generated by Django 5.1 on 2024-11-21 03:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0017_delete_actionlog'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('edit', '编辑'), ('delete', '删除')], max_length=10, verbose_name='操作类型')),
                ('target_id', models.IntegerField(verbose_name='操作目标ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('details', models.TextField(blank=True, verbose_name='操作详情')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作用户')),
            ],
        ),
    ]
