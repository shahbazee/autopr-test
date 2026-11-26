"""
Simple Django models module.
"""

from django.db import models


class Item(models.Model):
    """
    Example model representing an item with a name and timestamp.
    """
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
