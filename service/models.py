from django.db import models
from django.conf import settings


class Pancard(models.Model):
    WAITING = 'W'
    PROCESSING = 'P'
    COMPLETED = 'C'
    STATUS_CHOICES = [
        (WAITING, 'Waiting'),
        (PROCESSING, 'Processing'),
        (COMPLETED, 'Completed')
    ]

    TAMPERED = 'T'
    ORIGINAL = 'O'
    RESULT_CHOICES = [
        (TAMPERED, 'Tampered'),
        (ORIGINAL, 'Original')
    ]

    number = models.CharField(max_length=20, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    confidence = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=WAITING, null=True, blank=True)
    result = models.CharField(max_length=1, choices=RESULT_CHOICES, default=TAMPERED, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.number}"

    class Meta:
        get_latest_by = ['datetime']


class PancardImage(models.Model):
    pancard = models.ForeignKey(Pancard, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='service/images')
    diff = models.ImageField(upload_to='service/images', null=True, blank=True)
    thresh = models.ImageField(upload_to='service/images', null=True, blank=True)
    upload = models.ImageField(upload_to='service/images', null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        get_latest_by = ['datetime']


class PanOriginal(models.Model):
    image = models.ImageField(upload_to='service/images')