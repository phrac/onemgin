from celery import task
from words.models import Word
from nltk import pos_tag, word_tokenize
import re
from sorl.thumbnail import get_thumbnail

@task()
def process_words(wordstring):
    clean_title = re.sub(r'([^\s\w]|_)+', ' ', wordstring.lower())
    wordlist = pos_tag(word_tokenize(clean_title))
    for w in wordlist:
        if w[1] == 'NN' or w[1] == 'NNS' or w[1] == 'JJ':
            if len(w[0]) >= 3:
                word, created = Word.objects.get_or_create(word=w[0].strip().lower())
                
@task()
def generate_thumb(product, size):
    if product.image_url:
        get_thumbnail(product.image_url, size, crop='center')