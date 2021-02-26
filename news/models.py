from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, \
    GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


User = get_user_model()


class Vote(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name="votes", on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = GenericRelation(Vote)

    @property
    def amount_of_votes(self):
        return self.votes.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
