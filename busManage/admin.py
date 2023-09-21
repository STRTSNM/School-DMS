from django.contrib import admin
from .models import StudentList, BusRoute, BusStop

admin.site.register(StudentList)
admin.site.register(BusRoute)
admin.site.register(BusStop)

