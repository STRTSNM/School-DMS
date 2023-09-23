from django.shortcuts import render, redirect, get_object_or_404
from .models import BusRoute, BusStop, StudentList, BusRouteService
from .forms import StudentImportForm
from .models import StudentList
import pandas as pd
from datetime import date

Student=StudentList


def home_busManage(request):
    return render(request, 'busManage.html')

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



def upload_student_data(request):
    if request.method == 'POST':
        form = StudentImportForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']

            if excel_file.name.endswith('.xlsx'):
                df = pd.read_excel(excel_file)

                for index, row in df.iterrows():
                    name = row['Name']
                    classs = row['Class']
                    bus_route_name = row['Bus Route']
                    bus_stop_name = row['Bus Stop']

                    bus_route_instance, created = BusRoute.objects.get_or_create(name=bus_route_name)

                    bus_stop_instance, created = BusStop.objects.get_or_create(name=bus_stop_name, route=bus_route_instance)

                    student = StudentList(name=name, classs=classs, bus_route=bus_route_instance, bus_stop=bus_stop_instance)
                    student.save()

                return redirect('success_page')
    else:
        form = StudentImportForm()

    return render(request, 'upload_student_data.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')


def bus_route_service_list(request):
    bus_route_services = BusRouteService.objects.all()
    
    for service in bus_route_services:
        if not service.is_serviced:
            days_until_service = (service.next_service_date - date.today()).days
            service.days_until_service = days_until_service
    
    return render(request, 'bus_route_service_list.html', {'bus_route_services': bus_route_services})

def mark_as_serviced(request, service_id):
    service = get_object_or_404(BusRouteService, pk=service_id)
    if not service.is_serviced:
        service.is_serviced = True
        service.mark_as_serviced()
        service.save()
    return redirect('bus_route_service_list')