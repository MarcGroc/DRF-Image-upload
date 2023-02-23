from django.contrib.auth.models import User
from django.test import TestCase

from rest_api.models import Image, Tier


class ImageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.image = {
            "id": 1,
            "original_image": "test.jpg",
            "t200": "test.jpg",
            "t400": "test.jpg",
            "created_at": "2021-05-01 12:00:00",
            "uploaded_by": self.user.pk,
            "link_expiration_time": 300,
        }

    def test_image_model_data_should_be_valid(self):
        self.assertEqual(self.image["original_image"], "test.jpg")
        self.assertEqual(self.image["t200"], "test.jpg")
        self.assertEqual(self.image["t400"], "test.jpg")
        self.assertEqual(self.image["created_at"], "2021-05-01 12:00:00")
        self.assertEqual(self.image["uploaded_by"], self.user.pk)
        self.assertEqual(self.image["link_expiration_time"], 300)

    def test_should_raise_error_if_image_extension_not_png_or_jpg(self):
        self.image["original_image"] = "test.sh"
        self.assertRaises(ValueError, Image.objects.create, **self.image)
        self.image["original_image"] = "test.php"
        self.assertRaises(ValueError, Image.objects.create, **self.image)
        self.image["original_image"] = "test.py"
        self.assertRaises(ValueError, Image.objects.create, **self.image)

    def test_should_raise_error_if_link_expiration_time_is_not_between_300_and_3000(
        self,
    ):
        self.image["link_expiration_time"] = 299
        self.assertRaises(ValueError, Image.objects.create, **self.image)
        self.image["link_expiration_time"] = 3001
        self.assertRaises(ValueError, Image.objects.create, **self.image)


class TierModelTest(TestCase):
    def setUp(self):
        self.tier = {
            "name": "test",
            "thumbnail_200": True,
            "thumbnail_400": False,
            "original_image_link": False,
            "link_expiration": False,
        }

    def test_tier_model_data_should_be_valid(self):
        self.assertEqual(self.tier["name"], "test")
        self.assertEqual(self.tier["thumbnail_200"], True)
        self.assertEqual(self.tier["thumbnail_400"], False)
        self.assertEqual(self.tier["original_image_link"], False)
        self.assertEqual(self.tier["link_expiration"], False)


class AccountTierModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.tier = Tier.objects.create(
            name="test",
            thumbnail_200=True,
            thumbnail_400=False,
            original_image_link=False,
            link_expiration=False,
        )
        self.account_tier = {
            "user": self.user.pk,
            "tier": self.tier.pk,
        }

    def test_account_tier_model_data_should_be_valid(self):
        self.assertEqual(self.account_tier["user"], self.user.pk)
        self.assertEqual(self.account_tier["tier"], self.tier.pk)
