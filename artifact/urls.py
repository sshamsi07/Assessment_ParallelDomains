from django.urls import path
from artifact.views import SingleArtifactBySlug, ArtifactByQueryParameters, CreateArtifact

urlpatterns = [
    # fetches lists based on specified query params
    path('', ArtifactByQueryParameters.as_view(), name='artifact-list'), #
    path('create', CreateArtifact.as_view(), name='artifact-post'),
    path('<str:slug>', SingleArtifactBySlug.as_view(), name='artifact-get'),
]