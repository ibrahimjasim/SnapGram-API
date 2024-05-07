from rest_framework import serializers
from django.utils import timezone
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    organizer_username = serializers.ReadOnlyField(source='organizer.username')  # Display organizer's username

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'location', 'start_time', 'end_time', 'organizer', 'organizer_username', 'created_at', 'updated_at',"website","admission_price"]
        read_only_fields = ['organizer', 'created_at', 'updated_at']  # These fields should not be editable by the API

    def validate_start_time(self, value):
        """
        Check that the start_time is not in the past.
        """
        if value < timezone.now():
            raise serializers.ValidationError("Start time cannot be in the past.")
        return value

    def validate(self, data):
        """
        Check that the end time is later than the start time.
        """
        if data['end_time'] <= data['start_time']:
            raise serializers.ValidationError({"end_time": "End time must be after the start time."})
        return data

    def create(self, validated_data):
        """
        Create and return a new Event instance, given the validated data.
        """
        # The organizer is set in the view's perform_create method
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Event instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.location = validated_data.get('location', instance.location)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.website = validated_data.get('website', instance.website)
        instance.admission_price = validated_data.get('admission_price', instance.admission_price)

        instance.save()
        return instance