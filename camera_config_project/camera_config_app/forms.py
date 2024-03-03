from django import forms

class CameraFeedForm(forms.Form):
    camera_url = forms.URLField(label='Camera URL', max_length=100)

