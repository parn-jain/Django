from django.contrib import admin
from django.urls import path,include
from .views import * 
from django.urls import re_path
urlpatterns = [
    path('',home,name = "home"),
    path('student/',StudentAPI.as_view()),
    


    # path('student/',post_student,name= "post_student"),
    # path('update-student/<id>',update_student),
    # path('delete-student/<id>',delete_student)
    # re_path(r'^delete-student/$',delete_student)
]
