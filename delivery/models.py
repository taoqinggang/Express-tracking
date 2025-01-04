from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class DailyQueryCount(models.Model):
    query_date = models.DateField(default=timezone.now)
    query_count = models.PositiveIntegerField(default=0)

    @classmethod
    def increment_count(cls):
        today = timezone.now().date()
        record, created = cls.objects.get_or_create(query_date=today)
        if record.query_count < 30:
            record.query_count += 1
            record.save()
            return True  # 表示可以查询
        return False  # 达到上限，禁止查询



class Delivery(models.Model):
    username = models.CharField(max_length=100)
    fill_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=200)
    sent_tracking_number = models.CharField(max_length=50, blank=True, null=True)
    return_tracking_number = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.username