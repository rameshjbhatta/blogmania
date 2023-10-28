from rest_framework import serializers
from blogapp.models import *

class BlogInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = BlogInfo  
            fields = '__all__' 


class ContactInfoSerializer(serializers.ModelSerializer):
      class Meta:
            model=ContactInfo
            fields='__all__'