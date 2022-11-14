from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=64)


class CardSet(models.Model):
    name = models.CharField(max_length=150)
    authorId = models.BigIntegerField


class Flashcard(models.Model):
    cardSetId = models.BigIntegerField
    front = models.CharField(max_length=255)
    back = models.TextField(max_length=1024)


class Favorite(models.Model):
    userId = models.BigIntegerField
    cardSetId = models.BigIntegerField

