from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'omniflash_users'


class CardSet(models.Model):
    name = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'omniflash_card_sets'


class Flashcard(models.Model):
    card_set = models.ForeignKey(CardSet, on_delete=models.CASCADE)
    front = models.CharField(max_length=255)
    back = models.TextField(max_length=1024)

    class Meta:
        db_table = 'omniflash_flashcards'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_set = models.ForeignKey(CardSet, on_delete=models.CASCADE)

    class Meta:
        db_table = 'omniflash_favorites'


class Category(models.Model):
    name = models.enums

    class Meta:
        db_table = 'omniflash_categories'


class SetCategory(models.Model):
    card_set = models.ForeignKey(CardSet, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'omniflash_set_category'

