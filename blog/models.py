from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,    # ✅ allows author to be empty
        blank=True    # ✅ makes it optional in admin/forms
    )
    content = models.TextField()

    def __str__(self):
        return self.title
