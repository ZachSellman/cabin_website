from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """Profile class is one to one with Users model such that there can only be one profile per user."""

    # Cascade mean that if the model is delete, then we also delete
    # the profile, but if we delete the profile it will not delete the user

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"
