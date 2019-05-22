"""Quotes Models"""
from django.db import models

# Create your models here.
class Quote(models.Model):
    """Creates Quote class"""
    text = models.TextField(unique=True, blank=False)
    quote_len = 0

    def __str__(self):
        if len(self.text) > 20:
            return self.text[:20] + "..."
        else:
            return self.text

    def save(self, *args, **kwargs):
        self.quote_len = len(self.text)
        super(Quote, self).save(*args, **kwargs)
