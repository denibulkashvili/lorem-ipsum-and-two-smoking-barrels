"""Quotes Models"""
from django.db import models

# Create your models here.
class Quote(models.Model):
    """Creates Quote class"""
    text = models.TextField(unique=False, blank=False)
    quote_len = models.IntegerField(blank=True, default=1)
    movie = models.TextField(default="Lock, Stock and Two Smoking Barrels")

    def __str__(self):
        if len(self.text) > 20:
            return self.text[:20] + "..."
        return self.text

    # def save(self, *args, **kwargs):
    #     self.quote_len = len(self.text)
    #     super(Quote, self).save(*args, **kwargs)
