from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    active = models.BooleanField(default=True)
    published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("articles:detail",kwargs = {"id":self.id})
    
    def get_absolute_edit_url(self):
        return reverse("articles:edit", kwargs={"id":self.id})