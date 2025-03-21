from django.contrib import admin
from django.utils.html import format_html  # Allows displaying images in the panel
from .models import Candidate, Voter, Vote

class CandidateAdmin(admin.ModelAdmin):
    list_display = ("name", "party", "bio", "display_photo")  # Show bio & photo in list

    def display_photo(self, obj):
        if obj.photo:  # Check if photo exists
            return format_html('<img src="{}" width="50" height="50" style="border-radius:10px;" />', obj.photo.url)
        return "No Image"
    display_photo.short_description = "Photo"  # Column name in admin panel

admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Voter)
admin.site.register(Vote)
