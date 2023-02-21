import io
import json
from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from PIL import Image as PILImage
from rest_framework.test import APITestCase

from rest_api.models import AccountTier, ArbitraryTier, Image, Tier


def fake_image():
    image_to_upload = PILImage.new("RGB", (256, 256), "red")
    bytes_obj = BytesIO()
    image_to_upload.save(bytes_obj, "JPEG")
    bytes_obj.seek(io.SEEK_SET)
    return SimpleUploadedFile("test.jpg", bytes_obj.read(), content_type="image/JPEG")


class ImageModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.tier = Tier.objects.create(name="test")
        self.account_tier = AccountTier.objects.create(user=self.user, tier=self.tier)
        self.img = fake_image()
        self.image = {
            "original_image": self.img,
            "t200": "test.jpg",
            "t400": "test.jpg",
            "created_at": "2021-05-01 12:00:00",
            "temporary_link": "http://test.com",
            "uploaded_by": self.user.pk,
            "link_expiration_time": 300,
        }
        self.client.force_authenticate(user=self.user, token=None)

    def test_should_return_201(self):
        response = self.client.post(
            reverse("image-list"),
            self.image,
            format="multipart",
        )
        self.assertEqual(response.status_code, 201)

    def test_should_return_400_if_not_image(self):
        self.image["original_image"] = "test.jpg"
        response = self.client.post(
            reverse("image-list"),
            self.image,
            format="multipart",
        )
        self.assertEqual(response.status_code, 400)


class TierModelTest(APITestCase):
    def setUp(self):
        self.tier = {
            "name": "test",
            "thumbnail_200": True,
            "thumbnail_400": False,
            "original_image_link": False,
            "link_expiration": False,
        }

    def test_should_return_201(self):
        response = self.client.post(
            reverse("tier-list"),
            json.dumps(self.tier),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Tier.objects.count(), 1)

    def test_should_return_400_if_tier_already_exists(self):
        response = self.client.post(
            reverse("tier-list"),
            json.dumps(self.tier),
            content_type="application/json",
        )
        self.assertEqual(Tier.objects.count(), 1)
        response = self.client.post(
            reverse("tier-list"),
            json.dumps(self.tier),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)


class AccountTierModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.tier = Tier.objects.create(name="test")
        self.account_tier = {
            "user": self.user.pk,
            "tier": self.tier.pk,
        }

    def test_should_return_201(self):
        response = self.client.post(
            reverse("account-tier-list"),
            json.dumps(self.account_tier),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(AccountTier.objects.count(), 1)


class ArbitraryTierModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.image = Image.objects.create(
            original_image=fake_image(), uploaded_by=self.user
        )
        self.tier = Tier.objects.create(name="test")
        self.arbitrary_tier = {
            "name": "test",
            "thumbnail_size": 200,
            "original_image_link": self.image.pk,
            "link_expiration_time": 300,
        }

    def test_should_return_201(self):
        response = self.client.post(
            reverse("arbitrary-tier-list"),
            self.arbitrary_tier,
            format="multipart",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ArbitraryTier.objects.count(), 1)
