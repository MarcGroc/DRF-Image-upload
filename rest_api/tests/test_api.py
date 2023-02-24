import io
from io import BytesIO
from unittest import TestCase

from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

# from django.urls import reverse
from PIL import Image as PILImage

from rest_api.admin import AccountTierAdmin, TierAdmin
from rest_api.models import AccountTier, Tier


# from rest_framework.test import APITestCase


def fake_image():
    image_to_upload = PILImage.new("RGB", (256, 256), "red")
    bytes_obj = BytesIO()
    image_to_upload.save(bytes_obj, "JPEG")
    bytes_obj.seek(io.SEEK_SET)
    return SimpleUploadedFile("test.jpg", bytes_obj.read(), content_type="image/JPEG")


# class ImageModelTest(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="test", password="test")
#         self.tier = Tier.objects.create(name="test")
#         self.account_tier = AccountTier.objects.create(user=self.user, tier=self.tier)
#         self.img = fake_image()
#         self.image = {
#             "original_image": self.img,
#             "t200": "test.jpg",
#             "t400": "test.jpg",
#             "created_at": "2021-05-01 12:00:00",
#             "temporary_link": "http://test.com",
#             "uploaded_by": self.user.pk,
#             "link_expiration_time": 300,
#         }
#         self.client.force_authenticate(user=self.user, token=None)
#
#     def test_should_return_201(self):
#         response = self.client.post(
#             reverse("image-list"),
#             self.image,
#             format="multipart",
#         )
#         self.assertEqual(response.status_code, 201)
#
#     def test_should_return_400_if_not_image(self):
#         self.image["original_image"] = "test.jpg"
#         response = self.client.post(
#             reverse("image-list"),
#             self.image,
#             format="multipart",
#         )
#         self.assertEqual(response.status_code, 400)


class TierAdminTest(TestCase):
    def test_list_display(self):
        tier = Tier.objects.create(name="Tier 1")

        # Set up the TierAdmin class
        admin_site = AdminSite()
        tier_admin = TierAdmin(tier, admin_site)

        expected_display = [
            "name",
            "thumbnail_200",
            "thumbnail_400",
            "original_image_link",
            "custom_thumbnail",
        ]
        self.assertEqual(tier_admin.list_display, expected_display)


class AccountTierAdminTest(TestCase):
    def test_list_display(self):
        user = User.objects.create_user(username="test", password="test")
        tier = Tier.objects.create(name="Basic")
        account_tier = AccountTier.objects.create(user=user, tier=tier)

        admin_site = AdminSite()
        account_tier_admin = AccountTierAdmin(account_tier, admin_site)

        expected_display = ["user", "tier", "id"]
        self.assertEqual(account_tier_admin.list_display, expected_display)
