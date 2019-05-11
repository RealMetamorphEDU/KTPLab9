# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return "%s: %s" % (self.author.username, self.title)
    def get_excerpt(self):
        if len(self.text) > 140:
            return self.text[:140] + "..."
        else:
            return self.text
