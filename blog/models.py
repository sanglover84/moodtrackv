from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    mood = models.IntegerField() # title, mood on a scale of 1 -10
    feelings = models.CharField(max_length=200) 
    energy = models.IntegerField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # date

    def get_absolute_url(self):
        # Replace 'post-detail' with the actual 'name' of your detail URL path
        return reverse('post_detail', kwargs={'pk': self.pk})

def __str__(self):
    return self.mood

#def get_absolute_url(self):
  #  return reverse("post_detail", kwargs={"pk":self.pk})

