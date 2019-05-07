from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Permission

from .models import Poll, Question, Choice, Comment, Shop, UserProfile, ShopArea

admin.site.register(Permission)

admin.site.register(Shop)
admin.site.register(UserProfile)


class AreaAdmin(admin.ModelAdmin):
    list_display = ['area_code','isBooking','shop_owner', 'approve_status']
    list_per_page = 15

    search_fields = ['area_code','isBooking','shop_owner', 'approve_status']
    list_filter = ['isBooking', 'approve_status']




admin.site.register(ShopArea, AreaAdmin)
