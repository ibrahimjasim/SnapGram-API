from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'start_time', 'end_time', 'location')
    list_filter = ('start_time', 'end_time', 'organizer')
    search_fields = ('title', 'description', 'organizer__username')
    date_hierarchy = 'start_time'
    ordering = ('-start_time',)
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        """
        Function to modify the queryset returned for the list display. This can be customized
        to show different results based on user permissions or other criteria.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(organizer=request.user)
