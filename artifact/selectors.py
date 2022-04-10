import json

from django.db.models.functions import Lower
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.exceptions import ParseError
from artifact.serializers import ArtifactSerializer
from artifact.models import Artifact


class ArtifactByQueryParameters(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ArtifactSerializer

    def get_queryset(self, category=None, platform_used=None):
        if self.request.method == 'GET':
            queryset = Artifact.objects.all()
            # To allow case insensitive querying from query parameters
            category = self.request.query_params.get('category', default="").lower()
            platform_used = self.request.query_params.get('platform', default="").lower()

            if category or platform_used :
                if category not in list(Artifact.objects.values_list('category', flat=True).distinct()) or \
                        platform_used not in list(Artifact.objects.values_list('platform_used', flat=True).distinct()):
                    raise ParseError("values not supplied")
                queryset = Artifact.objects.filter(category__icontains=category,
                                                   platform_used__icontains=platform_used)
            return queryset


class SingleArtifactBySlug(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ArtifactSerializer

    def get_queryset(self, **kwargs):
        slug = self.kwargs['slug']
        if slug not in list(Artifact.objects.values_list('slug',flat=True)):
            raise ParseError("In correct slug value")
        return Artifact.objects.filter(slug=slug)


class CreateArtifact(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        artifact_data = json.loads(request.body)
        artifact_serializer = ArtifactSerializer(data=artifact_data)

        if artifact_serializer.is_valid():
            artifact_serializer.save()
            return Response(artifact_serializer.data, status=HTTP_201_CREATED)
        return Response(artifact_serializer.errors, status=HTTP_400_BAD_REQUEST)