
from django.urls import path,include
from . import views
urlpatterns = [
    path('index/',views.index),
    path('country/',views.show_by_country),
    path('choosecountry/',views.show_by_country),
    path('india/',views.india),
    path('usa/',views.usa),
    path('newzealand/',views.newzealand),
    path('australia/',views.australia),
    path('blogcount/',views.blogcount),
]
