from django.shortcuts import render
from .models import BusRoute, BusStop, StudentList

def select_data(request):
    bus_routes = BusRoute.objects.all()
    bus_stops = BusStop.objects.all()
    class_choices = [
        (None, 'None'), 
        ('xii', 'XII'),
        ('xi', 'XI'),
        ('x', 'X'),
    ]

    selected_class = request.POST.get('class') if request.method == 'POST' else None
    selected_route_id = request.POST.get('bus_route') if request.method == 'POST' else None
    selected_stop_id = request.POST.get('bus_stop') if request.method == 'POST' else None
    students = []

    filter_conditions = {}
    if selected_class:
        if selected_class != 'None':  
            filter_conditions['classs'] = selected_class
    if selected_route_id:
        filter_conditions['bus_route_id'] = selected_route_id
    if selected_stop_id:
        filter_conditions['bus_stop_id'] = selected_stop_id

    if filter_conditions:
        students = StudentList.objects.filter(**filter_conditions)
    else:
        students = StudentList.objects.all()

    return render(request, 'select_data.html', {
        'bus_routes': bus_routes,
        'bus_stops': bus_stops,
        'class_choices': class_choices,
        'selected_class': selected_class,
        'selected_route_id': selected_route_id,
        'selected_stop_id': selected_stop_id,
        'students': students,
    })
