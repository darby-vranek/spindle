from django.contrib import admin
from .models import Character, Post, Verse


admin.site.register(Character, admin.ModelAdmin)
admin.site.register(Post, admin.ModelAdmin)
admin.site.register(Verse, admin.ModelAdmin)
