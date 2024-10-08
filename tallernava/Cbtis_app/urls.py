from django.urls import path
from Cbtis_app import views
urlpatterns = [

    path('',views.indexvista,name="indexvista"),
]