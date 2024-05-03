from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.analytics_report, name='analytics_report'),
]
