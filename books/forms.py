from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']

        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative")
        return quantity

    def clean_price(self):
        price = self.cleaned_data['price']

        if price < 0:
            raise forms.ValidationError("Price cannot be negative")
        return price
