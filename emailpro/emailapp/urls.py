from django.urls import path,include
from emailapp.views import test

urlpatterns = [

    path('hello/', view=test,name='test'),
]
