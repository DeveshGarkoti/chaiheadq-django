from django.contrib import admin
from .models import Tweet
# Register your models here.


class TweetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('text',)}

admin.site.register(Tweet, TweetAdmin)
