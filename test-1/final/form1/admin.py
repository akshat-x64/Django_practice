from django.contrib import admin
from form1.models import form1
# Register your models here.


class form__1(admin.ModelAdmin):
    list_display = ('name1','eamil1','phone1','website1','message1',)


admin.site.register(form1,form__1)