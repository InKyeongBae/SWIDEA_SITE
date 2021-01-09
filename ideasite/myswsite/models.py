from django.db import models
from django.shortcuts import reverse

# Create your models here.
class DevTool(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("myswsite:devtool_read", kwargs={"pk": self.pk})


class Idea(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="image")
    content = models.TextField(null=True, blank=True)
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE, null=True, related_name="idea")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("myswsite:idea_read", kwargs={"pk": self.pk})
    

