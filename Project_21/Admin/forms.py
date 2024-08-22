from django import forms
from .models import Items

class ItemForm(forms.ModelForm):
    class Meta:
        model=Items
        fields=['item_name','itms_desc','item_price','item_image']