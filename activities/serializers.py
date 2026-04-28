from rest_framework import serializers
from activities.models import Event, EventCategory, Venue

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ['id','name','description']

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ['id','name','address','city','country','created_at']

class EventSerializer(serializers.ModelSerializer):
    category = EventCategorySerializer(read_only=True)
    venue = VenueSerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = '__all__'
    
    def create(self, validated_data):
        # Handle nested category creation if provided
        category_data = validated_data.pop('category', None)
        if category_data:
            # Check if category already exists by name
            category, created = EventCategory.objects.get_or_create(
                name=category_data['name'],
                defaults=category_data
            )
            validated_data['category'] = category
        
        # Handle nested venue creation if provided
        venue_data = validated_data.pop('venue', None)
        if venue_data:
            # Check if venue already exists by name
            venue, created = Venue.objects.get_or_create(
                name=venue_data['name'],
                defaults=venue_data
            )
            validated_data['venue'] = venue
        
        return Event.objects.create(**validated_data)