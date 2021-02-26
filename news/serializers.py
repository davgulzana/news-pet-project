from rest_framework import serializers

from news.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    creation_date = serializers.DateTimeField(read_only=True)
    amount_of_upvotes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["amount_of_votes"] = instance.amount_of_votes
        return representation


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    creation_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
