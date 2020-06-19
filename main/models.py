from django.db import models

import re
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["nameLabel"]) < 2:
            errors["nameLabel"] = "First Name must be at least 2 characters"
        if len(postData["aliasLabel"]) < 2:
            errors["aliasLabel"] = "Alias be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['emailLabel']):
            errors['emailLabel'] = "Invalid email address!"
        if len(postData["passwordLabel"]) < 8:
            errors["passwordLabel"] = "Password must be at least 8 characters"
        if postData["passwordLabel"] != postData["passwordConfirmLabel"]:
            errors['pw_confirm'] = "Passwords must match!!"
        return errors


class User(models.Model):
    name = models.CharField(max_length=64)
    alias = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #book_uploaded
    #reviews
    objects = UserManager()


class Author(models.Model):
    name = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #books

class Book(models.Model):
    title = models.CharField(max_length=64)
    #reviews

    uploaded_by = models.ForeignKey(
        User,
        related_name="books_uploaded",
        on_delete = models.CASCADE
    )
    author = models.ForeignKey(
        Author,
        related_name = "books",
        on_delete = models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.CharField(max_length=64)

    reviewer = models.ForeignKey(
        User,
        related_name = "reviews",
        on_delete = models.CASCADE
    )
    book_reviews = models.ForeignKey(
        Book,
        related_name="reviewer",
        on_delete = models.CASCADE


    )