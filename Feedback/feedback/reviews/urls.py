from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.ReviewView.as_view()),
    path("thank-you",views.tyView.as_view()),
    path("review",views.ReviewsListView.as_view(), name = "list-review"),
    path("review/<int:id>",views.SingleReviewView.as_view(), name = 'single-review')
]

