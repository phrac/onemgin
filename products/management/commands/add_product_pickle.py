from django.core.management.base import BaseCommand, CommandError
import pickle
from django.conf import settings

class Command(BaseCommand):
    args = '<product string>'
    help = 'Adds a product word to the product pickle file'
    can_import_settings = True
    
    def handle(self, *args, **options):
        pkl = open(settings.PRODUCT_PICKLE_FILE, 'r+')
        words = pickle.load(pkl)
        words.append(args[0])
        pickle.dump(words, pkl)
        pkl.close()
