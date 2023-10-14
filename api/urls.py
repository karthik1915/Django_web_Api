from django.urls import path
from . import views

urlpatterns = [
    path("",views.IndexView),
    path("api/",views.ApiView,name="Api Index Page"),
    path("about/",views.AboutView,name="about"),
    path("contact/",views.ContactView,name="contact"),
    #
    # Images API Urls 
    #
    path("api/images",views.ImagesView,name="Images_API"),
    path("api/images.json",views.ImagesApiView.as_view(),name="Images_Json"),
    path("api/images/random/", views.RandomImageView.as_view(), name="random-image"),
    path("api/images/gallery",views.ImagesGallery,name="Gallery"),
    path("api/images/upload",views.createimage,name="upload"),
    #
    # Scapping Urls
    #
    path("scraps/",views.scraps_view,name="scraps index"),
    path("scraps/images/gelbooru",views.getgelbooru,name="gelbooru scraps")
    #
    #
    #
]