from amazon.api import AmazonAPI
from django.conf import settings
from products.models import Product
from words.models import Word
from random import choice, randint
from products.tasks import process_words, generate_thumb

def process_browse_node(browse_node_list):
    """Processes browse node list

    Used to create and fetch the category ID for a product's browse node

    :return:
        An instance of :class:`products.Category` representing the most
        specific category.
    """
    pass
    
def fetch_random():
    search_noun = Word.objects.order_by('?')[0]
    search_adj = Word.objects.exclude(word=search_noun.word).order_by('?')[0]
    search_term = "%s %s" % (search_adj, search_noun)
    print search_term
    amazon = AmazonAPI(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, settings.AWS_ASSOCIATE_TAG)
    products = amazon.search_n(5, Keywords="%s" % search_term, SearchIndex='All')
    return products, search_term
    
def validate_product(product):
    if product.upc and product.ean:
        return True
    else:
        return False

def random_product():
    products, search_term = fetch_random()
    i = 0
    print len(products)
    if len(products) == 0:
        return None, None
    else:
        product = products[i]
    while validate_product(product) is not True:
        if i > len(products)-1:
            return None, None
        product = products[i]
        i += 1
    print i
    return (product.asin, search_term)

def get_or_create_product(asin):
    try:
        product = Product.objects.get(asin=asin)
    except:
        amazon = AmazonAPI(settings.AWS_ACCESS_KEY_ID,
                           settings.AWS_SECRET_ACCESS_KEY,
                           settings.AWS_ASSOCIATE_TAG)                                       
        az = amazon.lookup(ItemId=asin)
        product = Product(asin=asin, upc=az.upc, ean=az.ean, 
                          description=az.title, image_url=az.large_image_url,
                          amazon_url=az.offer_url)
    
        product.manufacturer = az.get_attribute('Manufacturer')
        product.brand = az.get_attribute('Brand')
        product.model_number = az.get_attribute('Model')
        product.mpn = az.mpn
        product.part_number = az.part_number
        product.sku = az.sku
        product.isbn = az.isbn
        product.length = az.get_attribute('ItemDimensions.Length')
        product.width = az.get_attribute('ItemDimensions.Width')
        product.height = az.get_attribute('ItemDimensions.Height')
        product.weight = az.get_attribute('ItemDimensions.Weight')
        product.save()
        generate_thumb.delay(product, '600x400')

        
    return product


    
