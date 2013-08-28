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
    
    product.manufacturer = az.get_attribute('Manufacturer')
    product.brand = az.get_attribute('Brand')
    product.model_number = az.get_attribute('Model')
    product.mpn = az.get_attribute('MPN')
    product.sku = az.sku
    product.isbn = az.isbn
    product.length = az.get_attribute('ItemDimensions.Length')
    product.width = az.get_attribute('ItemDimensions.Width')
    product.height = az.get_attribute('ItemDimensions.Height')
    product.weight = az.get_attribute('ItemDimensions.Weight')
    product.save()
        
    return product  
    
