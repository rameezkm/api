from django.shortcuts import render
from django.http import JsonResponse
from . serializer import ApiSerializer
from . models import Api
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def index(request):
    if request.method=="GET":
        api=Api.objects.all()
        serializer = ApiSerializer(api, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method=="POST":
        serializer=ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
@api_view(["GET","DELETE"])
def detail(request, id):
    try:
        api=Api.objects.get(id=id)
    except:
        return JsonResponse({'err':' data not found'})
    if request.method=="GET":
        serializer=ApiSerializer(api)
        return JsonResponse(serializer.data, safe=False)
    if request.method=="DELETE":
        api.delete()
        return JsonResponse({'deleted':'data deleted'}, status=204)
    