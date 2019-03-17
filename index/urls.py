from django.urls import path
from . import views
# start with index
urlpatterns = [
    # http://localhost:8000/index/
    path('', views.index, name='index'),
    path('download.html', views.download,name = 'download'),
]