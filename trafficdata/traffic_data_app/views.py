from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from .models import TrafficData
import csv
from .utils.ReadCSV import readCSV  # Add this line
from django.shortcuts import redirect
from .forms import TrafficDataForm
from django.shortcuts import get_object_or_404

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

def reload_data(request):
    global traffic_data
    traffic_data = readCSV()
    messages.success(request, 'Data reloaded successfully')
    return render(request, 'reload.html', {'message': 'Data persisted successfully'})
    # return JsonResponse({'message': 'Data reloaded successfully'})

def persist_data(request):
    with open('exported_traffic_data.csv', 'w', newline='') as file:
        traffic_data = readCSV()
        writer = csv.writer(file)
        writer.writerow(["sectionID", "highway", "section", "sectionLength", "sectionDescription", "date", "description", "group", "type", "county", "ptrucks", "adt", "direction"])
        for data in traffic_data:
            writer.writerow([data.get_sectionID(), data.get_highway(), data.get_section(), data.get_sectionLength(), data.get_sectionDescription(), data.get_date(), data.get_description(), data.get_group(), data.get_type(), data.get_county(), data.get_ptrucks(), data.get_adt(), data.get_direction()])
    messages.success(request, 'Data persisted successfully')
    return render(request, 'exported.html', {'message': 'Data persisted successfully'})
    # return JsonResponse({'message': 'Data persisted successfully'})

def edit_data(request, id):
    data = get_object_or_404(TrafficData, pk=id)
    if request.method == "POST":
        form = TrafficDataForm(request.POST, instance=data)
        if form.is_valid():
            data = form.save()
            data.save()
            return redirect('traffic_data_view')
    else:
        form = TrafficDataForm(instance=data)
    return render(request, 'edit.html', {'form': form})

def delete_data(request, id):
    data = get_object_or_404(TrafficData, pk=id)
    if request.method == "POST":
        data.delete()
        return redirect('traffic_data_view')
    return render(request, 'confirm_delete.html', {'object': data})

def delete_selected_data(request):
    selected_data_ids = request.POST.getlist('selected_data')
    TrafficData.objects.filter(id__in=selected_data_ids).delete()
    return redirect('traffic_data_view')