# camera_config_app/forms.py
from django import forms

class CameraFeedForm(forms.Form):
    # Define your form fields here
    camera_url = forms.URLField(label='Camera URL', max_length=100)
    # Add other form fields as needed
