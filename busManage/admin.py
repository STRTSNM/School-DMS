from django.contrib import admin
from .models import StudentList, BusRoute, BusStop, BusRouteService

admin.site.register(StudentList)
admin.site.register(BusRoute)
admin.site.register(BusStop)
admin.site.register(BusRouteService)

