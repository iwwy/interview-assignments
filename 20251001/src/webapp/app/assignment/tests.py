from django.test import Client, TestCase

from .forms import ProductSearchForm
from .models import Product


class ProductSearchFormTest(TestCase):
    fixtures = ["assignment.json"]

    def test_product_search_form_invalid_data(self):
        form = ProductSearchForm({"tags": "invalid"})
        self.assertFalse(form.is_valid())

    def test_product_search_form_empty(self):
        form = ProductSearchForm({})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.filters(), {})

    def test_product_search_form_with_data(self):
        form = ProductSearchForm({
            "category": [1, 2],
            "tags": [3, 4],
            "name": "a",
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.filters(), {
            "category__in": ["1", "2"],
            "tags__in": ["3", "4"],
            "name__icontains": "a",
        })


class AssignmentTest(TestCase):
    fixtures = ["assignment.json"]

    def test_products_present_in_db(self):
        self.assertEqual(Product.objects.count(), 20)

    def test_products_search_view_name(self):
        client = Client()
        response = client.get("/products/", {"name": "Phone"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "assignment/products.html")
        self.assertEqual(response.context["products"][0].name, "Phone")
