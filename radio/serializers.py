from rest_framework import serializers
from .models import Artist, Hit

class ArtistSerializer(serializers.ModelSerializer):
    # Serialize Artist object to JSON and back
    class Meta:
        model = Artist
        fields = ['id', 'first_name', 'last_name', 'created_at']

class HitSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(), source='artist', write_only=True
    )

    class Meta:
        model = Hit
        fields = [
            'id', 'title', 'artist', 'artist_id', 'title_url',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'title_url']

    def create(self, validated_data):
        # Generates title_url based on track title
        from django.utils.text import slugify
        title = validated_data['title']
        validated_data['title_url'] = slugify(title)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Updates tite_url if title changed
        if 'title' in validated_data:
            from django.utils.text import slugify
            instance.title_url = slugify(validated_data['title'])
        return super().update(instance, validated_data)
