import random , requests
from django.shortcuts import HttpResponse,render
from rest_framework import generics
from .models import ImagesModel
from .serializers import ImagesModelSerializer
from rest_framework.response import Response

def IndexView(request):
    return(HttpResponse("hello <a href='api'>api</a>"))

def ApiView(request):
    return render(request, 'base.html')

#
# Images Views
#

def ImagesView(request):
    url = "http://127.0.0.1:8000/api/images/random/?is_safe=true"
    response = requests.get(url)

    if response.status_code == 200:
        api_data = response.json()
        context = {"title":"Images" , "api_response": api_data, "status_code": response.status_code}
        return render(request, "images.html", context)
    else:
        context = {
            "api_response": False,
            "status_code": response.status_code,
        }
        return render(request, "images.html", context)


class ImagesApiView(generics.ListAPIView):
    queryset = ImagesModel.objects.all()
    serializer_class = ImagesModelSerializer

    def get_queryset(self):
        is_safe_param = self.request.query_params.get('is_safe')
        if is_safe_param is not None:
            is_safe = is_safe_param.lower() == 'true'
            return ImagesModel.objects.filter(is_safe=is_safe)

        return ImagesModel.objects.all()

class RandomImageView(generics.ListAPIView):
    serializer_class = ImagesModelSerializer

    def get_queryset(self):
        is_safe_param = self.request.query_params.get('is_safe')
        queryset = ImagesModel.objects.all()

        if is_safe_param is not None:
            is_safe = is_safe_param.lower() == 'true'
            queryset = queryset.filter(is_safe=is_safe)

        if queryset.exists():
            return [random.choice(queryset)]
        else:
            return []

