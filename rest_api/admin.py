from django.contrib import admin

from .models import AccountTier, Image, Tier


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        "uploaded_by",
        "created_at",
        "original_image",
        "t200",
        "t400",
        "link_expiration_time",
        "custom_thumbnail",
        # "custom_thumbnail_size",
    ]


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "thumbnail_200",
        "thumbnail_400",
        "original_image_link",
        "custom_thumbnail",
    ]


@admin.register(AccountTier)
class AccountTierAdmin(admin.ModelAdmin):
    list_display = ["user", "tier", "id"]
