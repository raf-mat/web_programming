from django import forms

class NewListing(forms.Form):
    title = forms.CharField(max_length=50)
    category = forms.CharField(max_length=70)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':80, 'size':8}), label="Text Area")
    starting_bid = forms.IntegerField()
    image = forms.ImageField(required=False)
