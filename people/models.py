from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    info = models.TextField()
    active = models.BooleanField(default=True)

class Entry(models.Model):
    content = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    subject = models.ForeignKey(Person)
