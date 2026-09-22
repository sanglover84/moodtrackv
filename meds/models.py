from django.db import models
from django.urls import reverse
# Create your models here.

class MedsPost(models.Model):
    medname = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    generic = models.CharField(max_length=200)
    totaldose = models.IntegerField()
    dose1 = models.IntegerField()
    dose2 = models.IntegerField()
    dose3 = models.IntegerField()
    frequency = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    whatfor = models.TextField()
    sideeffects = models.TextField()

    def __str__(self):
        return self.medname

    def get_absolute_url(self):
        return reverse("medspost_detail",kwargs={"pk":self.pk})
