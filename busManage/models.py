from django.db import models

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
