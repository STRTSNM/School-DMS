from django.db import models
from django.utils import timezone

class BusRoute(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BusStop(models.Model):
    name = models.CharField(max_length=100)
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE, related_name='bus_stops')

    def __str__(self):
        return self.name

class StudentList(models.Model):
    CLASS_CHOICES = [
        ('xii', 'XII'),
        ('xi', 'XI'),
        ('x', 'X'),
    ]
    
    name = models.CharField(max_length=200)
    classs = models.CharField(max_length=100, choices=CLASS_CHOICES)
    bus_route = models.ForeignKey(BusRoute, on_delete=models.SET_NULL, null=True, blank=True)
    bus_stop = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class BusRouteService(models.Model):
    bus_route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)  
    last_service_date = models.DateField()
    next_service_date = models.DateField()
    is_serviced = models.BooleanField(default=False)

    def calculate_next_service_date(self):
        if self.last_service_date:
            return self.last_service_date + timezone.timedelta(days=180)
        return None

    def mark_as_serviced(self):
        self.is_serviced = True
        self.next_service_date = self.calculate_next_service_date()

    def save(self, *args, **kwargs):
        if self.is_serviced:
            self.mark_as_serviced()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Service for {self.bus_route.name} on {self.last_service_date}"
