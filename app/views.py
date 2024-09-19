from datetime import datetime
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app.models import *
from app.serializers import *

@csrf_exempt
def get_location(request,id=0):
    if request.method == "POST":
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            place_name = get_place_name(latitude, longitude)
            if place_name:
                locationModel = location()
                locationModel.latitude = latitude
                locationModel.longitude = longitude
                locationModel.location = place_name
                locationModel.date = datetime.now().date()
                locationModel.time = datetime.now().time()
                locationModel.save()
                return JsonResponse({'status': 'success', 'place_name': place_name})
            else:
                
                return JsonResponse({'status': 'error', 'message': 'Could not find place name'}, status=404)
    elif request.method == "GET":
        locationModel = location.objects.last()
        serializer = LocationSerializer(locationModel)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "DELETE":
        if id:
            locationModel = location.objects.filter(id=id)
            locationModel.delete()
            return JsonResponse({"success":True},status=200)
        else:
            locationModel = location.objects.all()
            for locations in locationModel:
                locations.delete()
            return JsonResponse({"success":True},status=200)    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


def get_place_name(latitude, longitude):
    try:
        headers = {
            'User-Agent': 'YourAppName/1.0 (your.email@example.com)'  
        }
        response = requests.get(
            f'https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json',
            headers=headers
        )
        data = response.json()
        return data.get('display_name')  
    except Exception as e:
        print(f"Error retrieving place name: {e}")
        return None

def alllocation(request):
    if request.method == "GET":
        locationModel = location.objects.all().order_by('time')
        serializer = LocationSerializer(locationModel,many=True)
        return JsonResponse(serializer.data,safe=False)