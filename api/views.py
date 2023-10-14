import random , requests 
from bs4 import BeautifulSoup
from django.shortcuts import render ,redirect
from rest_framework import generics
from .models import ImagesModel
from .serializers import ImagesModelSerializer
from .forms import UploadImage

def IndexView(request):
    return render(request,'main_index.html')

def ApiView(request):
    context = {"title":"API"}
    return render(request, 'base.html',context=context)

def AboutView(request):
    return render(request,'about.html')

def ContactView(request):
    return render(request,'contact.html')

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

def ImagesGallery(request):
    url = "http://127.0.0.1:8000/api/images.json"
    response = requests.get(url)

    if response.status_code == 200:
        api_data = response.json()
        context = {"title":"Images" , "api_response": api_data, "status_code": response.status_code}
        return render(request, "gallery.html", context)
    else:
        context = {
            "api_response": False,
            "status_code": response.status_code,
        }
        return render(request, "gallery.html", context)

def createimage(request):
    if request.POST:
        form = UploadImage(request.POST, request.FILES)
        if form.is_valid():
            tags_input = form.cleaned_data['tags']
            tags_set = set(tags_input.split(',')) 
            tags_list = list(tags_set)
            model_instance = form.save(commit=False)
            model_instance.tags = tags_list
            model_instance.save()
            return redirect("/api/images/gallery")
    return render(request, 'upload.html', {'form': UploadImage})

#
#   scraps 
#

def scraps_view(request):
    return render(request, 'scraps.html')

def getgelbooru(request):
    url = 'https://gelbooru.com/index.php?page=post&s=list&tags=all'
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    else:
        print(f"Failed to retrieve the web page (Status Code: {response.status_code})")

    article = soup.find_all("article")
    context = []
    src,title_list=[],[]

    for item in article:
        img = item.find('img')
        src.append(img.get('src'))
        title_list.append(img.get('title'))
    
    for i in range(0,len(src)):
        sub_context = {"image": src[i] , "category":title_list[i]}
        context.append(sub_context)

    data_dict = {index: item for index, item in enumerate(context, start=1)}


    apiresponse = {
        "api_response": data_dict,
    }

    return render(request, "gelbooru.html" ,apiresponse)
