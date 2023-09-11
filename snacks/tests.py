from django.test import TestCase
from django.urls import reverse
from .models import Snack


class SnackListViewTests(TestCase):
    def test_snack_list_view_status_code(self):
        url = reverse('snack_list')  # Assuming 'snack_list' is the name of the URL pattern for SnackListView
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_view_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')  # Assuming 'snack_list.html' is the template name

    def test_snack_list_view_url_name(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


