from django.urls import path
from . import views

urlpatterns = [
    path("",views.IndexView),
    path("api/",views.ApiView,name="Api Index Page"),
    #
    # Images API Urls 
    #
    path("api/images.json",views.ImagesApiView.as_view(),name="Images API"),
    path("api/images",views.ImagesView,name="Images API"),
    path("api/images/random/", views.RandomImageView.as_view(), name="random-image"),
    path("api/images/gallery",views.ImagesGallery,name="Gallery")
    #
    #
    #
]