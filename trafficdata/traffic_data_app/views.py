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
    traffic_data = load_data(request)
    return render(request, 'traffic_data.html', {'traffic_data': traffic_data})

def reload_data(request):
    traffic_data = TrafficData.objects.all()
    return render(request, 'traffic_data.html', {'traffic_data': traffic_data})

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
            return redirect('trafficdata')
    else:
        form = TrafficDataForm(instance=data)
    return render(request, 'edit.html', {'form': form})

def delete_data(request, id):
    data = get_object_or_404(TrafficData, pk=id)
    if request.method == "GET":
        data.delete()
        data.save()
        # TrafficData.objects.filter(id=id).delete()
        return redirect('trafficdata')
    return redirect('trafficdata')

def delete_selected_data(request):
    selected_data_ids = request.POST.getlist('selected_data')
    TrafficData.objects.filter(id__in=selected_data_ids).delete()
    return redirect('trafficdata')

def load_data(request):
    dtos = readCSV()
    traffic_data_list = []  # Create an empty list to store the TrafficData objects
    for dto in dtos:
        data = TrafficData(
            id=dto.get_id(),
            sectionID=dto.get_sectionID(),
            highway=dto.get_highway(),
            section=dto.get_section(),
            sectionLength=dto.get_sectionLength(),
            sectionDescription=dto.get_sectionDescription(),
            date=dto.get_date(),
            description=dto.get_description(),
            group=dto.get_group(),
            type=dto.get_type(),
            county=dto.get_county(),
            # ptrucks=dto.get_ptrucks(),
            adt=dto.get_adt(),
            # aadt=dto.get_aadt(),
            direction=dto.get_direction(),
            # pct85=dto.get_85pct(),
            # priorityPoints=dto.get_priorityPoints()
        )
        data.save()
        traffic_data_list.append(data)  # Add the TrafficData object to the list

    return render(request, 'traffic_data.html', {'traffic_data': TrafficData.objects.all()})

# def load_data(request):
#     dtos = readCSV()
#     for dto in dtos:
#         data = TrafficData(
#             id=dto.get_id(),
#             sectionID=dto.get_sectionID(),
#             highway=dto.get_highway(),
#             section=dto.get_section(),
#             sectionLength=dto.get_sectionLength(),
#             sectionDescription=dto.get_sectionDescription(),
#             date=dto.get_date(),
#             description=dto.get_description(),
#             group=dto.get_group(),
#             type=dto.get_type(),
#             county=dto.get_county(),
#             # ptrucks=dto.get_ptrucks(),
#             adt=dto.get_adt(),
#             # aadt=dto.get_aadt(),
#             direction=dto.get_direction(),
#             # pct85=dto.get_85pct(),
#             # priorityPoints=dto.get_priorityPoints()
#         )
#         data.save()
#     return redirect('traffic_data_view')