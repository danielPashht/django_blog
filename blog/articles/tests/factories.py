import factory.fuzzy
from articles.models import Post


class PostFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Post
		django_get_or_create = ('title',)

	title = factory.Faker('sentence', nb_words=4)
	content = factory.Faker('text')
	author = factory.Faker('name')
