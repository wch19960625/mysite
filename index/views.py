from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse,Http404
# Create your views here.
def index(request):
    username = request.user.username
    return render(request,'index.html',locals())
def download(request):
    file = open('index\static\setup.zip','rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition']='attachment;filename="sepup.zip"'
    return response