from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user.username')
    
    class Meta:
        model = Post
        fields = (
            'text',
            'owner',
            'created_at'
        )