from django.contrib.contenttypes.models import ContentType

from news.models import Vote


def add_vote(obj, user):
    """
    To add a vote from the user to the Post object.
    One user can only vote once.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    vote, is_created = Vote.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user
    )
    return vote


def remove_vote(obj, user):
    """
    To remove a vote from the user to the Post object.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    Vote.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()


def reset_all_votes():
    """
    To remove all votes from Vote model for reset votes count of posts.
    """
    Vote.objects.all().delete()
