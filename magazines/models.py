from django.db import models

MONTH_CHOICES = (
    ('January', 'Jan'),
    ('February', 'Feb'),
    ('March', 'Mar'),
)
class Magazine(models.Model):
    month = models.CharField(max_length=10, choices=MONTH_CHOICES, default='jan')
    image = models.ImageField(upload_to="images", blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    alt_img = models.CharField(max_length=255, blank=True, null=True)