from django.db import models


class PageVisit(models.Model):
    # db -> Table
    # id -> primary key -> autofield -> 1,2,3
    path = models.TextField(blank=True, null=True) #column
    timestamp = models.DateTimeField(auto_now_add=True) #column
