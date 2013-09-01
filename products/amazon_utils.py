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
    
def fetch_random(num_results=5):
    """
    Build a random search term of 2-3 words and perform an Amazon product
    search.

    :return:
        An instance of :class:`amazon.api.AmazonSearch`
    """

    search_term = ''
    words = Word.objects.order_by('?')[:randint(2,3)]
    for word in words:
        search_term = "%s %s" % (word, search_term.strip())
    print search_term
    amazon = AmazonAPI(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, settings.AWS_ASSOCIATE_TAG)
    products = amazon.search_n(num_results, Keywords="%s" % search_term, SearchIndex='All')
    return products, search_term
    
def validate_product(product):
    """ 
    Validates the presence of an EAN and UPC of
    :class:`amazon.api.AmazonProduct`

    :return:
        Boolean
    """
    if product.upc and product.ean:
        return True
    else:
        return False

def random_product():
    """
    Iterates through a list of Amazon products, finding the first product that
    contains a UPC and EAN

    :return:
        An Amazon ASIN
    """
    products, search_term = fetch_random()
    i = 0
    if len(products) == 0:
        return None, None
    else:
        product = products[i]
    while validate_product(product) is not True:
        if i > len(products)-1:
            return None, None
        product = products[i]
        i += 1
    process_words.delay(product.title)
    return (product.asin, search_term)

def get_or_create_product(asin):
    """
    Checks the database for an existing ASIN. If not found, try to fetch it
    using the Amazon Product API.

    :return:
        An instance of `products.models.Product`
    """
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
        
        product.save()
        generate_thumb.delay(product, '600x400')
        generate_thumb.delay(product, '125x125')
    
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
        

        
    return product


    
