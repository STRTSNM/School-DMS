from django.urls import path
from . import views

urlpatterns = [
    path('select-data/', views.select_data, name='select_data'),
]
