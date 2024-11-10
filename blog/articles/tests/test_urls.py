from django.test import SimpleTestCase
from django.urls import reverse, resolve
from articles.views import add_post, edit_post, post, index


class TestUrls(SimpleTestCase):

    def test_urls(self):
        views = [add_post, edit_post, post, index]
        urls = [
            reverse('add_post'),
            reverse('edit_post', args=[1]),  # Provide a post_id argument
            reverse('post', args=[1]),       # Provide a post_id argument
            reverse('index')
        ]

        for url, view in zip(urls, views):
            self.assertEquals(resolve(url).func, view)
