from django.contrib import admin
from .models import Profile
#ADD
# from .models import BlogArticle

class ProfileAdmin(admin.ModelAdmin):
    class meta:
        model = Profile
# Register your models here.
admin.site.register(Profile,ProfileAdmin)
# admin.site.register(BlogArticle)
#ADD 
