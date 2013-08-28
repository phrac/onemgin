from amazon.api import AmazonAPI
from django.conf import settings
from products.models import Product

def get_or_create_product(asin):
    amazon = AmazonAPI(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, settings.AWS_ASSOCIATE_TAG)
    az = amazon.lookup(ItemId=asin)
    try:
        product = Product.objects.get(asin=asin)
        if not product.amazon_url:
            product.amazon_url = az.offer_url
    except:
        product = Product(asin=asin, upc=az.upc, ean=az.ean, 
                          description=az.title, image_url=az.large_image_url,
                          amazon_url=az.offer_url)
    product.save()
        
    return product  
    
