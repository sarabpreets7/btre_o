from django.contrib import admin

# Register your models here.
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date','is_mvp')
    list_display_links = ('id','name')
    list_per_page = 25


admin.site.register(Realtor,RealtorAdmin)