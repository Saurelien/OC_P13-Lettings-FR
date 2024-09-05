from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile


class IndexTestCase(TestCase):
    def test_index(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')

    def test_profile_with_valid_username(self):
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'Paris')
        self.assertContains(response, self.user.username)

    def test_profile_not_found_returns_404(self):
        response = self.client.get('/profiles/nonexistent-user/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

