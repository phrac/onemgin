from amazon.api import AmazonAPI
from django.conf import settings
from products.models import Product
from sorl.thumbnail import get_thumbnail
from random import choice, randint
import pickle
from nltk import pos_tag, word_tokenize

def process_browse_node(browse_node_list):
    """Processes browse node list

    Used to create and fetch the category ID for a product's browse node

    :return:
        An instance of :class:`products.Category` representing the most
        specific category.
    """
    pass

def random_product():
    pkl = open(settings.PRODUCT_PICKLE_FILE, 'r+')
    words = pickle.load(pkl)
    word = choice(words)
    pkl.close()
    print "Searching %s" % word
    amazon = AmazonAPI(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, settings.AWS_ASSOCIATE_TAG)
    products = amazon.search_n(20, Keywords="%s" % word, SearchIndex='All')
    count = len(products)
    product = products[randint(0,count-1)]
    valid = None
    while not valid:
        product = products[randint(0,count-1)]
        if product.ean and product.upc:
            valid = 1
    
    wordlist = pos_tag(word_tokenize(product.title.lower()))
    for w in wordlist:
        if w[1] == 'NN' or w[1] == 'NNS':
            if w[0] not in words and len(w[0]) >= 3:
                print "Appending %s" % w[0]
                words.append(w[0])
    pkl = open(settings.PRODUCT_PICKLE_FILE, 'w').close()
    pkl = open(settings.PRODUCT_PICKLE_FILE, 'w+')
    pkl.truncate()
    pickle.dump(words, pkl)
    pkl.close()
    return product.asin

def get_or_create_product(asin):
    try:
        product = Product.objects.get(asin=asin)
        print 'not in db'
    except:
        amazon = AmazonAPI(settings.AWS_ACCESS_KEY_ID,
                           settings.AWS_SECRET_ACCESS_KEY,
                           settings.AWS_ASSOCIATE_TAG)                                       
        az = amazon.lookup(ItemId=asin)
        print 'got product'
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
        print 'product saved'
        if product.image_url:
            get_thumbnail(product.image_url, '600x400', crop='center')

        
    return product


    
