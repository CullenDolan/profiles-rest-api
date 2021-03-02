from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing oir APIView"""
    """accepts name input to test POST functionality"""
    name = serializers.CharField(max_length=10)
    
