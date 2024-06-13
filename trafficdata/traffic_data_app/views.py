from django.shortcuts import render
from .models import TrafficData
from .utils.ReadCSV import readCSV  # Add this line

traffic_data = []

def index(request):  # Add this function
    # return render(request, 'traffic_data.html')
    traffic_data = readCSV()
    return render(request, 'traffic_data.html', {'traffic_data': traffic_data})

def traffic_data_view(request):
    # fileName = "./traffic_data_app/data/Traffic_Volumes_-_Provincial_Highway_System.csv"
    # fileName = "../data/Traffic_Volumes_-_Provincial_Highway_System.csv"
    traffic_data = readCSV()
    return render(request, 'traffic_data.html', {'traffic_data': traffic_data})