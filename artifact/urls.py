from django.urls import path
from artifact.selectors import SingleArtifactBySlug, ArtifactByQueryParameters, CreateArtifact
urlpatterns = [
    path('', ArtifactByQueryParameters.as_view()),
    path('create', CreateArtifact.as_view()),
    path('<str:slug>', SingleArtifactBySlug.as_view()),


]