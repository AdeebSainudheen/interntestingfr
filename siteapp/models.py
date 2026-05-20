from django.db import models
from django.urls import reverse


class Product(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	short_description = models.CharField(max_length=255, blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image_url = models.CharField(max_length=500, blank=True)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product_detail', args=[self.slug])
