from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):  # Cegah hashing ulang
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)