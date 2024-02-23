from django.urls import path
from .views import index, presentation


urlpatterns = [
    path('index/', index, name='my_app-index'),
    path('presentation/', presentation, name='my_app-presentation')
    
    
   
]