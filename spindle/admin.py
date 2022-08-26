from django.contrib import admin
from .models import Character, Post, Verse, Thread, Reply


admin.site.register(Character, admin.ModelAdmin)
admin.site.register(Post, admin.ModelAdmin)
admin.site.register(Verse, admin.ModelAdmin)
admin.site.register(Thread, admin.ModelAdmin)
admin.site.register(Reply, admin.ModelAdmin)
