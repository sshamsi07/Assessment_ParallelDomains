from faker import Faker
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


from artifact.test.artifact_factory import ArtifactFactory


class ArtifactTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        """
        Setting up testing framework using artifact_factory module
        :return:
        """
        super().setUpClass()
        cls.artifact_object = ArtifactFactory.build()
        cls.artifact_saved = ArtifactFactory.create()
        cls.client = APIClient()
        cls.fetch_list_url = reverse('artifact-list')
        cls.post_url = reverse('artifact-post')
        cls.faker_obj = Faker()

    def test_create_artifact(self):
        # Prepare data
        post_artifact_dict = {
            'slug': self.artifact_object.slug,
            'category': self.artifact_object.category,
            'platform_used': self.artifact_object.platform_used
        }
        # Make request
        response = self.client.post(self.post_url, post_artifact_dict)

        # Check Response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['slug'], post_artifact_dict['slug'])

    def test_create_artifact_already_exists(self):
        # Prepare data with already saved artifact
        post_artifact_dict = {
            'slug': self.artifact_saved.slug,
            'category': self.artifact_saved.category,
            'platform_used': self.artifact_saved.platform_used
        }
        # Make request
        response = self.client.post(self.post_url, post_artifact_dict)

        # Check Response
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['slug'][0]), 'artifact with this slug already exists.')

    def test_fetch_artifact_list(self):

        # Make request to fetch artifact list
        response = self.client.get(self.fetch_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['slug'], self.artifact_saved.slug)

    def test_get_query_param_artifact(self):

        # Prepare url for fetching artifact based on query parameters
        testing_url = "/artifacts/?category={}&platform={}".\
            format(self.artifact_saved.category, self.artifact_saved.platform_used)

        # Make request
        response = self.client.get(testing_url)

        # Check Response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['category'], self.artifact_saved.category)
