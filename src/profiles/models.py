from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Image by <a href="https://pixabay.com/users/wingtilldie-3058071/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1577909">WingTillDie</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1577909">Pixabay</a>
# can only be one profile for each user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    bio = models.TextField(blank=True)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"profile of the user {self.user.username}"
