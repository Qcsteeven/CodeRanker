from django.core.management.base import BaseCommand
from scraper.utils import scrape_chitai_gorod, scrape_tiobe_index
from scraper.models import Language, Book

class Command(BaseCommand):
    help = "Scrape data and populate the database"

    def handle(self, *args, **kwargs):
        if not Language.objects.exists() and not Book.objects.exists():
            Language.objects.all().delete()
            Book.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Database is empty, starting scraping..."))
            scrape_tiobe_index()
            languages = Language.objects.all()
            for language in languages:
                scrape_chitai_gorod(language.name)
            self.stdout.write(self.style.SUCCESS("Scraping completed!"))
        else:
            self.stdout.write(self.style.SUCCESS("Database is not empty, skipping scraping."))
