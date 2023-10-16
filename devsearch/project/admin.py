from django.contrib import admin
from .models import project,Tag,review

# Register your models here.
admin.site.register(project)
admin.site.register(Tag)
admin.site.register(review)