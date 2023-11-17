from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from blog.models import BlogModel
from blog.serializer import BlogSerializer
# from django.db.models import Q




@csrf_exempt
def add(request):
    if request.method=="POST":
        received_data=json.loads(request.body)
        print(received_data)

        check=BlogSerializer(data=received_data)
        if check.is_valid():
            check.save()
            return HttpResponse(json.dumps({"status":"success"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))


@csrf_exempt
def view(request):
    if request.method=="POST":
        blogList=BlogModel.objects.all()
        serialized=BlogSerializer(blogList,many=True)
        return HttpResponse(json.dumps(serialized.data))
