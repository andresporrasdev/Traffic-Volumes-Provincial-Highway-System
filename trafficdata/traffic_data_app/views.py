from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from .models import TrafficData
import csv
from .utils.ReadCSV import readCSV
from django.shortcuts import redirect
from .forms import TrafficDataForm
from django.shortcuts import get_object_or_404

traffic_data = []

def index(request):
    """
    This function is the view for the index page of the traffic data app.
    It reads a CSV file containing traffic data and renders the 'traffic_data.html' template,
    passing the traffic data as a context variable.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    FileName="D:/Git/PythonLearning/PythonLearning/trafficdata/traffic_data_app/data/Traffic_Volumes_-_Provincial_Highway_System.csv"
    traffic_data = readCSV(FileName)
    return render(request, 'traffic_data.html', {'traffic_data': traffic_data})

def traffic_data_view(request):
    """
    View function for displaying traffic data.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template with the traffic data.

    """
    traffic_data = TrafficData.objects.all()
    return render(request, 'traffic_data.html', {'traffic_data': traffic_data})

def reload_data(request):
    """
    Reloads traffic data and renders it on the traffic_data.html template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML response containing the traffic data.

    """
    traffic_data = TrafficData.objects.all()
    return render(request, 'traffic_data.html', {'traffic_data': traffic_data})

def persist_data(request):
    """
    Persists traffic data to a CSV file.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template with a success message.

    Raises:
        None
    """
    with open('exported_traffic_data.csv', 'w', newline='') as file:
        fileName = "D:/Git/PythonLearning/PythonLearning/trafficdata/traffic_data_app/data/Traffic_Volumes_-_Provincial_Highway_System.csv"
        traffic_data = readCSV(fileName)
        writer = csv.writer(file)
        writer.writerow(["sectionID", "highway", "section", "sectionLength", "sectionDescription", "date", "description", "group", "type", "county", "ptrucks", "adt", "direction"])
        for data in traffic_data:
            writer.writerow([data.get_sectionID(), data.get_highway(), data.get_section(), data.get_sectionLength(), data.get_sectionDescription(), data.get_date(), data.get_description(), data.get_group(), data.get_type(), data.get_county(), data.get_ptrucks(), data.get_adt(), data.get_direction()])
    messages.success(request, 'Data persisted successfully')
    return render(request, 'exported.html', {'message': 'Your data have been exported succesfully'})
    # return JsonResponse({'message': 'Data persisted successfully'})

def edit_data(request, id):
    """
    Edit the traffic data with the given id.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The id of the traffic data to be edited.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        Http404: If the traffic data with the given id does not exist.
    """
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
    """
    Delete the traffic data with the given ID.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the traffic data to be deleted.

    Returns:
        HttpResponse: The HTTP response containing the rendered 'traffic_data.html' template
                      with the updated traffic data.

    """
    data = request.GET.getlist(id)
    TrafficData.objects.filter(id__in=data).delete()
    traffic_data = TrafficData.objects.all()  # Get the current data in memory
    return render(request, 'traffic_data.html', {'traffic_data': traffic_data})  # Render the current data

def insert_data(request):
    """
    View function to handle the insertion of traffic data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    if request.method == "POST":
        form = TrafficDataForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('trafficdata')
    else:
        form = TrafficDataForm()
    return render(request, 'edit.html', {'form': form})

def delete_selected_data(request):
    """
    Deletes the selected traffic data from the database.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered traffic data.

    """
    selected_data_ids = request.POST.getlist('selected_data')
    TrafficData.objects.filter(id__in=selected_data_ids).delete()
    traffic_data = TrafficData.objects.all()  # Get the current data in memory
    return render(request, 'traffic_data.html', {'traffic_data': traffic_data})  # Render the current data

def load_data(request):
    """
    Loads traffic data from a CSV file and saves it to the database.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template with the traffic data.

    """
    fileName = "D:/Git/PythonLearning/PythonLearning/trafficdata/traffic_data_app/data/Traffic_Volumes_-_Provincial_Highway_System.csv"
    dtos = readCSV(fileName)
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

def display_selected_data(request):
    """
    Display the selected traffic data.

    This function takes a request object and retrieves the selected data IDs from the POST parameters.
    It then queries the TrafficData model to get the selected data and renders it in the 'traffic_data.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered 'traffic_data.html' template with the selected data.

    """
    selected_data_ids = request.POST.getlist('selected_data')
    traffic_data = TrafficData.objects.filter(id__in=selected_data_ids) # Get the selection
    return render(request, 'traffic_data.html', {'traffic_data': traffic_data})  # Render the current data