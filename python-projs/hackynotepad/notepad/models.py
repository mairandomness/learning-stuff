import datetime

from django.db import models
from django.utils import timezone


class Note(models.Model):
    note_title = models.CharField(max_length=200, blank=False)
    pub_date = models.DateTimeField('date published')
    note_author = models.CharField(max_length=100, blank=False)
    note_body = models.TextField('text', blank=False)

    def __str__(self):
        return self.note_title

    # class Meta:
    #     permissions(("can_edit",),
    #                 ("can_delete",),
    #                 ("can_read",),)

