from django.contrib import admin

from .models import AccountTier, Image, Tier


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["uploaded_by", "created_at", "original_image", "t200", "t400"]


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "thumbnail_200",
        "thumbnail_400",
        "original_image_link",
        "link_expiration_time",
    ]


@admin.register(AccountTier)
class AccountTierAdmin(admin.ModelAdmin):
    list_display = ["user", "tier"]
