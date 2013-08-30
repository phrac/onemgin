from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=25)
    type = models.ForeignKey('WordType')

    def __unicode__(self):
        return self.word

class WordType(models.Model):
    type = models.CharField(max_length=25)

    def __unicode__(self):
        return self.type
