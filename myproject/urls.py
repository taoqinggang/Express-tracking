from django.urls import path
from delivery import views
from django.contrib import admin
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('import_excel/', views.import_excel, name='import-excel'),
    path('download_sample/', views.download_sample, name='download-sample'),
    path('batch_delete/', views.batch_delete, name='batch-delete'),
    path('search_by_phone/', views.search_by_phone, name='search-by-phone'),
    path('', views.login_view, name='login'),
    path("track_delivery/", views.track_delivery, name="track_delivery"),
    path('list/', views.DeliveryListView.as_view(), name='delivery-list'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('add/', views.DeliveryCreateView.as_view(), name='delivery-add'),
    path('update/<int:pk>/', views.DeliveryUpdateView.as_view(), name='delivery-update'),
    path('delete/<int:pk>/', views.DeliveryDeleteView.as_view(), name='delivery-delete'),
]
