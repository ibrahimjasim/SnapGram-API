from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    It includes dynamic fields that depend on the request context,
    such as ownership status and relationship details.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Returns True if the request user is the owner of the profile.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Returns the ID of a Follower
        instance if the request user is following this profile's owner,
        otherwise returns None.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'following_id',
            'posts_count', 'followers_count', 'following_count',
        ]
        