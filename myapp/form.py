from django import forms
from .models import ImageUpload

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['image']


class EditOptionsForm(forms.Form):  # Use forms.Form if not linked to a specific model
    number = forms.IntegerField(label='Enter a number', min_value=1, required=True)
    
    # You can add more fields if needed
    # For example, an optional text field
    comment = forms.CharField(label='Comment', required=False, max_length=200)

    def clean_number(self):
        data = self.cleaned_data['number']
        # Custom validation (if needed)
        if data < 0:
            raise forms.ValidationError("Number must be positive!")
        return data

    # If you want to process the data after submission
    def process_data(self):
        # Implement your logic to handle the number here
        number = self.cleaned_data['number']
        # Perform any operations based on the number
        return number  # Return whatever result you need
