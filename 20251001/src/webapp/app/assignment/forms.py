from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from taggit.models import Tag

from .models import Category


class ProductSearchForm(forms.Form):  # type: ignore
    """
    Form for searching products.

    Attributes:
        category (MultipleChoiceField): Category filter.
        tags (MultipleChoiceField): Tag filter.
        name (CharField): Description filter.
    """
    category = forms.MultipleChoiceField(
        label="Category",
        choices=Category.objects.values_list("id", "name"),
        widget=CheckboxSelectMultiple(),
        required=False,
    )
    tags = forms.MultipleChoiceField(
        label="Tags",
        choices=Tag.objects.values_list("id", "name"),
        widget=CheckboxSelectMultiple(),
        required=False,
    )
    name = forms.CharField(label="Description", max_length=255, required=False)

    def filters(self) -> dict:
        """return search filters as specified in the form"""
        return {
            field: self.cleaned_data[name]
            for field, name in (
                ("category__in", "category"),
                ("tags__in", "tags"),
                ("name__icontains", "name"),
            )
            if self.cleaned_data[name]
        }
