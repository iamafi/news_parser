from rest_framework import serializers


class ParserSerializer(serializers.Serializer):
    source = serializers.CharField(required=True)
    url = serializers.URLField(required=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        fields = ['source', 'url']
