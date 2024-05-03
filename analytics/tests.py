from django.test import TestCase
from django.contrib.auth.models import User
from .models import PageView

class AnalyticsTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        PageView.objects.create(user=user, url='/test-url/')
    
    def test_page_view_created(self):
        page_view = PageView.objects.get(url='/test-url/')
        self.assertIsNotNone(page_view)
