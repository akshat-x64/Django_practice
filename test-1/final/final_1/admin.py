from django.contrib import admin
from final_1.models import final_mode
# Register your models here.


class final_admin(admin.ModelAdmin):
    list_display = ('first_name','last_name','occ')


admin.site.register(final_mode,final_admin)