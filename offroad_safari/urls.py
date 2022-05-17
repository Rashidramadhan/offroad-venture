from django.urls import path
from .import views


urlpatterns = [
    # basic urls
    path('', views.home_page, name='home'),
    path('request-form', views.request_email, name='request_form'),
    path('package-list', views.packages_list, name='packages_list'),
    path('masai-mara', views.masai_mara, name='mara'),
    path('nairobi-ns', views.nairobi_nsp, name='nairobi_ns'),
    path('mount-kenya', views.mount_kenya, name='mount_kenya'),
    path('lake-nakuru', views.lake_nakuru, name='lake_nakuru'),
    path('tsavo-east', views.tsavo_east, name='tsavo_east'),
    path('tsavo-west', views.tsavo_west, name='tsavo_west'),
    path('naivasha', views.naivasha, name='naivasha'),
    path('pejeta', views.pejeta, name='pejeta'),
    path('amboseli', views.amboseli, name='amboseli'),
    ]