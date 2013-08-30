from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=25, unique=True)

    class Meta:
        ordering = ['word']

    def __unicode__(self):
        return self.word

