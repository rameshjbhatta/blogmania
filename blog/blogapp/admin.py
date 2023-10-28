from django.contrib import admin
from blogapp.models import BlogInfo,ContactInfo

# Register your models here.
class BlogInfoAdminView(admin.ModelAdmin):
  list_display=['title','img','content','date_time','author','type','related_to']

class ContactInfoAdminView(admin.ModelAdmin):
  list_display=['name','email','message']

admin.site.register(BlogInfo,BlogInfoAdminView)
admin.site.register(ContactInfo,ContactInfoAdminView)