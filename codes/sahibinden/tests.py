from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import models
# Create your tests here.

class SahibindenTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser'
            email='test@email.com'
            password = 'secret'
        )

        self.post = Post.objects.create(
            
            
        )
