from django.contrib import admin
from .models import GuestEnquiryModel
# Register your model


class GestEnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'package', 'news_letter', 'enquiry_message']
    list_filter = ['package']

admin.site.register(GuestEnquiryModel, GestEnquiryAdmin)

admin.site.site_header = 'Off Road Adventures Admin DashBoard'