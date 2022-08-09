from django.db import models


class BookManager(models.Manager):
    def sort_by_rate(self):
        return self.order_by('-rate')

    def free_books(self):
        return self.filter(free=True)


class Book(models.Model):
    name = models.CharField(max_length=10)
    rate = models.IntegerField(default=0)
    free = models.BooleanField(default=True)

    # CONFIG YOUR MODEL MANAGER HERE
    objects = models.Manager()
    books = BookManager()

    def __str__(self):
        return self.name
