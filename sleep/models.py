from django.db import models
from django.urls import reverse

# Create your models here.
class Sleep(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    hourssleep = models.IntegerField()
    notes = models.CharField(max_length=400)

    def __str__(self):
       return self.notes

    def get_absolute_url(self):
        return reverse("sleep_detail", kwargs={"pk":self.pk})

