from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Permission

from .models import Poll, Question, Choice, Comment, Shop, UserProfile, ShopArea, Review

admin.site.register(Permission)

admin.site.register(UserProfile)


class AreaAdmin(admin.ModelAdmin):
    list_display = ['area_code','isBooking','shop_owner', 'approve_status']
    list_per_page = 15


    search_fields = ['area_code','isBooking','shop_owner', 'approve_status']
    list_filter = ['isBooking', 'approve_status']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review_shop', 'review_title', 'review_message']
    search_fields = ['review_shop']

    list_filter = ['review_shop']
    list_per_page = 20


class ShopAdmin(admin.ModelAdmin):
    list_display = ['shop_name', 'shop_booking', 'shop_owner', 'shop_area']


admin.site.register(Shop, ShopAdmin)
admin.site.register(ShopArea, AreaAdmin)
admin.site.register(Review, ReviewAdmin)
