from django import forms
from .models import Delivery
class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['username', 'phone', 'address', 'sent_tracking_number', 'return_tracking_number']
        labels = {
            'username': '用户名',
            'phone': '手机号',
            'address': '地址',
            'sent_tracking_number': '快递单号【寄出】',
            'return_tracking_number': '快递单号【寄回】',
        }