from django.shortcuts import render
from .models import TrafficData

def index(request):  # Add this function
    return render(request, 'traffic_data.html')

def traffic_data_view(request):
    traffic_data = TrafficData.objects.all()
    return render(request, 'traffic_data.html', {'traffic_data': traffic_data})

