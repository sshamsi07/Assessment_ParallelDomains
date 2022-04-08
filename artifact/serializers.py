from rest_framework import serializers
from artifact.models import Artifact


class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ('slug', 'created', 'category', 'platform_used')
    #
    # def validate(self, attrs):
    #     if attrs['platform_used'] in ('Linux', 'Windows'):
    #         raise serializers.ValidationError({"platform_used":"Not among Linux and Windows"})
    #     return attrs


    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['platform_used'] not in ['Linux', 'Windows']:
            raise serializers.ValidationError("finish must occur after start")
        return data