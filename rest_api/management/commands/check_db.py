import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to check database connection"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        is_db_available = False
        while not is_db_available:
            try:
                connection.ensure_connection()
                is_db_available = True
            except OperationalError:
                self.stdout.write(
                    self.style.ERROR("Database unavailable, waiting 3 second...")
                )
                time.sleep(3)

        self.stdout.write(
            self.style.SUCCESS("Database available, and connection is established!")
        )
