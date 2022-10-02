import csv

from django.core.management.base import BaseCommand
from ingredients.models import Ingredients


class Command(BaseCommand):
    help = 'Loads ingredients from a csv file'

    def handle(self, *args, **options):
        with open(
            'ingredients/data/ingredients.csv', encoding='utf-8'
        ) as f:
            reader = csv.reader(f)
            for row in reader:
                name, unit = row
                Ingredients.objects.get_or_create(
                    name=name, measurement_unit=unit)
        self.stdout.write(
            self.style.SUCCESS('Successfully loaded ingredients'))
