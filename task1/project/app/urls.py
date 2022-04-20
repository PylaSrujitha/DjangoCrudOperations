from django.urls import path
from .views import *

urlpatterns=[ path('post/',Register.as_view()),
              path('get/',Getadmindetaiies.as_view()),
              path('getbyid/<int:Id>/',Getbyidadmindetaiies.as_view()),
              path('update/<int:Id>/',Updateadmindetailes.as_view()),
              path('Deletereg/<int:id>/',Deletereg.as_view()),

]