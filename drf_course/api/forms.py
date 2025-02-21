from django import forms

from api.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock')

    def clean_price(self):
        """" Field level validation for the price field """
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('Price cannot be negative')
        return price

    def clean_stock(self):
        """" Field level validation for the stock count field """
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError('Stock count cannot be negative')
        return stock
