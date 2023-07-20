from django.contrib import admin
from news.models import news
# Register your models here.


class newsAdmin(admin.ModelAdmin):
    list_display = ('news_title','news_description','news_image')

admin.site.register(news,newsAdmin)