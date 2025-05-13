from django.db import models


class AboutPage(models.Model):
    header = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.header
