from django.shortcuts import render
from .models import PageView

def analytics_report(request):
    page_views = PageView.objects.all()
    return render(request, 'analytics/report.html', {'page_views': page_views})


