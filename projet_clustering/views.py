from django.http.response import JsonResponse
from django.shortcuts import render


def my_view(request):
    
    return render(request, 'projet_clustering.html')

#def get_chart(_request):

    #chart={}

    #return JsonResponse(chart)