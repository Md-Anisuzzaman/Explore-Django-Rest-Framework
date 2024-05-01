from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.quiz_qu_view)
]
