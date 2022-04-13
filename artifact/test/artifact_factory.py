import factory.django
from factory import Faker

from artifact.models import Artifact

PLATFORM_VALUES = ['Linux', 'Windows']


class ArtifactFactory(factory.django.DjangoModelFactory):
    """
    Creating Artifact factory using factory boy and Faker libraries
    """
    class Meta:
        model = Artifact

    slug = Faker('slug')
    # Faker library defined 'word' formatter
    category = Faker('word')
    platform_used = Faker('random_element', elements=PLATFORM_VALUES)



