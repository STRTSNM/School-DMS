from django.shortcuts import render, redirect
from .models import BusRoute, BusStop, StudentList
from .forms import StudentImportForm
from .models import StudentList
import pandas as pd
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

            # Process the Excel file and add data to the database using Pandas
            if excel_file.name.endswith('.xlsx'):
                df = pd.read_excel(excel_file)

                for index, row in df.iterrows():
                    name = row['Name']
                    classs = row['Class']
                    bus_route_name = row['Bus Route']
                    bus_stop_name = row['Bus Stop']

                    # Retrieve the BusRoute instance based on the name
                    bus_route_instance, created = BusRoute.objects.get_or_create(name=bus_route_name)

                    # Retrieve the BusStop instance based on the name and route
                    bus_stop_instance, created = BusStop.objects.get_or_create(name=bus_stop_name, route=bus_route_instance)

                    student = StudentList(name=name, classs=classs, bus_route=bus_route_instance, bus_stop=bus_stop_instance)
                    student.save()

                return redirect('success_page')  # Redirect to a success page
    else:
        form = StudentImportForm()

    return render(request, 'upload_student_data.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')

