from django.db import models
from django.contrib.auth.models import User

class Petition(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="petitions")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="petition_images/", blank=True, null=True)  # 👈 new field

    @property
    def votes_count(self):
        return self.votes.count()

class Vote(models.Model):
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("petition", "user")
