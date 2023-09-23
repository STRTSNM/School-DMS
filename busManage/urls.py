from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_busManage, name='home_busManage'),
    path('select-data/', views.select_data, name='select_data'),
    path('upload/', views.upload_student_data, name='upload_student_data'),
    path('success/', views.success_page, name='success_page'),
    path('bus_route_service/', views.bus_route_service_list, name='bus_route_service_list'),
    path('mark_as_serviced/<int:service_id>/', views.mark_as_serviced, name='mark_as_serviced'),
]
