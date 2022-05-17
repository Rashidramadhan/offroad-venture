from django.db import models

# Create your models here.
class GuestEnquiryModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    package = models.CharField(max_length=100, null=True)
    news_letter = models.CharField(max_length=100, null=True)
    enquiry_message = models.TextField(null=True)
    extra_data = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'Guest_enquiry'