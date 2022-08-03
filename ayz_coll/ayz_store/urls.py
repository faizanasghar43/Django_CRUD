from django.urls import path

from . import views

urlpatterns = [
    path('employee', views.employee, name='employee'),
    path('', views.index, name='index'),
    path('customer', views.customer, name='customer'),
    path('order', views.orders_, name='orders_'),
    path('order/delete/<int:id>/', views.delete, name='delete'),
    path('employee/delete_emp/<int:id>/', views.delete_emp, name='delete_emp'),
    path('customer/delete_cus/<int:id>/', views.delete_cus, name='delete_cus'),
    path('customer/add_cus/', views.add_cus, name='add_cus'),
    path('employee/add_emp/', views.add_emp, name='add_emp'),
    path('order/add_order/', views.add_order, name='add_order'),
    path('employee/add_emp/add_record_emp/', views.add_record_emp, name='add_record_emp'),
    path('customer/add_cus/add_record_cus/', views.add_record_cus, name='add_record_cus'),
    path('order/add_order/add_record_order/', views.add_record_order, name='add_record_order'),
]
