from django.utils import timezone
from datetime import timedelta
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """SSerializer for the Notification model. 
    It includes a method to format the 'created_at' field, 
    enhancing its readability for users.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    sender = serializers.ReadOnlyField(source="sender.username")
    profile_image = serializers.ReadOnlyField(
        source="sender.profile.image.url"
    )
    item_id = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        if obj.created_at > timezone.now() - timedelta(days=1):
            return naturaltime(obj.created_at)
        else:
            return obj.created_at.strftime("%d %b %Y, %I:%M %p")

    class Meta:
        model = Notification
        fields = [
            "id",
            "owner",
            "sender",
            "profile_image",
            "created_at",
            "item_id",
            "is_read",
            "content",
            "category",
        ]