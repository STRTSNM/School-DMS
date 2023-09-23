from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_busManage, name='home_busManage'),
    path('select-data/', views.select_data, name='select_data'),
    path('upload/', views.upload_student_data, name='upload_student_data'),
    path('success/', views.success_page, name='success_page'),
]
