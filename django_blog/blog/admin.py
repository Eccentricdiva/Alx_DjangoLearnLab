from django.contrib import admin
from .models import Post   # import the model you created

# Register your model so it shows in the admin panel
admin.site.register(Post)
