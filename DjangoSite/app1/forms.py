from django import forms 

class StockForm(forms.Form):
    symbol = forms.CharField(label='Stock Symbol', max_length=10)