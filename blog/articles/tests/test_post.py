from django.test import TestCase
from django.contrib.auth.models import User
from .factories import PostFactory
from ..models import Post


class TestPosting(TestCase):

	def setUp(self):
		self.post = PostFactory()
		self.user = User.objects.create_user(
			username='testuser',
			password='12345',
		)

	def test_post_creation_success(self):
		self.client.login(username='testuser', password='12345')
		response = self.client.post('/add/', {
			'header': 'Test Title',
			'content': 'Test content',
			'author': self.user.username,
		})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, '/')
		self.assertEqual(response.wsgi_request.user, self.user)
		self.assertEqual(Post.objects.count(), 2)

	# ---- Not logged in test-cases ----

	def test_post_creation_not_logged_in(self):
		response = self.client.post('/add/', {
			'header': 'Test Title',
			'content': 'Test content',
			'author': self.user.username,
		})

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, '/login/?next=/add/')
		self.assertEqual(Post.objects.count(), 1)

	def test_post_edit_not_logged_in(self):
		response = self.client.post(f'/post/{self.post.id}/edit', {
			'header': 'Test Title',
			'content': 'Test content',
			'author': self.user.username,
		})

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, f'/login/?next=/edit/{self.post.id}/')

	def test_access_to_post_not_logged_in(self):
		response = self.client.get(f'/post/{self.post.id}/')

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, f'/login/?next=/post/{self.post.id}/')
