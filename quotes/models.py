"""Quotes Models"""
from django.db import models

# Create your models here.
class Quote(models.Model):
    """Creates Quote class"""
    MOVIE_CHOICES = [
        ("LOCK", "Lock, Stock and Two Smoking Barrels"),
        ("SNATCH", "Snatch"),
    ]
    text = models.TextField(unique=True, blank=False)
    quote_len = models.IntegerField(blank=True)
    movie = models.CharField(
        max_length=5,
        choices=MOVIE_CHOICES,
        default="LOCK"
    )

    def __str__(self):
        if len(self.text) > 20:
            return self.text[:20] + "..."
        return self.text

    def movie_verbose(self):
        return dict(Quote.MOVIE_CHOICES)[self.movie]

    def save(self, *args, **kwargs):
        self.quote_len = len(self.text)
        super(Quote, self).save(*args, **kwargs)
