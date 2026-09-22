from django.db import models
from django.urls import reverse

# Create your models here.
class Symptom(models.Model):
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    datetime = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=200)
    Anxiety = models.IntegerField()
    Depression = models.IntegerField()
    Mania = models.IntegerField()
    Paranoia = models.IntegerField()
    IdeasOfReference = models.IntegerField()
    Hallucinations = models.IntegerField()
    Fatigue = models.IntegerField()
    Insomnia = models.IntegerField()
    Restlessness = models.IntegerField()
    Agitation = models.IntegerField()
    WristPain = models.IntegerField()
    ShoulderPain = models.IntegerField()

    def __str__(self):
        return self.notes
    def get_absolute_url(self):
        return reverse("symptoms_detail",kwargs={"pk":self.pk})