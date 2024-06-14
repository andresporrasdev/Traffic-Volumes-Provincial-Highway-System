"""
URL configuration for trafficdata project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from traffic_data_app import views  # Correct import statement

urlpatterns = [
    path('', views.index, name='index'),  # Assuming 'index' is a function in your views.py
    path('trafficdata/', views.traffic_data_view, name='trafficdata'),  # Assuming 'traffic_data_view' is a function in your views.py
    path('reload/', views.reload_data, name='reload_data'),
    path('persist/', views.persist_data, name='persist_data'),
    path('edit/<int:id>/', views.edit_data, name='edit_data'),
    path('delete/<int:id>/', views.delete_data, name='delete_data'),
path('delete_selected/', views.delete_selected_data, name='delete_selected_data'),
]

# urlpatterns = [

#     path('admin/', admin.site.urls),
# ]