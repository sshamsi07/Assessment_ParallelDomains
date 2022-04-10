from rest_framework import serializers
from artifact.models import Artifact


class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ('slug', 'created', 'category', 'platform_used')
