"""Snippets app models"""

from django.contrib.auth import get_user_model
from django.db import models


class Snippet(models.Model):
    """Snippet model"""
    title = models.CharField('título', max_length=100)
    author = models.ForeignKey(
        verbose_name='autor',
        to=get_user_model(),
        on_delete=models.CASCADE
    )
    code = models.TextField('código')
    created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('fecha de actualización', auto_now=True)

    def __str__(self):
        """Returns snippet string """
        return '{} por @{}'.format(self.title, self.author.username)
