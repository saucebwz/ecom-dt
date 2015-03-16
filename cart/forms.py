from django import forms

class AddProductToCartForm(forms.Form):
    product_slug = forms.CharField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(widget=forms.TextInput(
                                  attrs={'size': '2',
                                         'value':'1', 'class': 'quantity', 'maxlength':'5'
                                        }
                                  ),
                                  error_messages={'Error!': 'Please enter a valid quantity.', 'max_value': 'Enter the valid quantity. Biggest quantity is 5'},
                                  min_value=1,
                                  max_value=5)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(AddProductToCartForm, self).__init__(*args, **kwargs)


    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Please, enable the cookies!")
        return self.cleaned_data