'''# camera_config_app/views.py
from django.shortcuts import render
from .forms import CameraFeedForm

def configure_camera_feed(request):
    if request.method == 'POST':
        form = CameraFeedForm(request.POST)
        if form.is_valid():
            camera_url = form.cleaned_data['camera_url']
            return render(request, 'camera_config_app/configure_camera_feed.html', {'form': form, 'camera_url': camera_url})
    else:
        form = CameraFeedForm()
    return render(request, 'camera_config_app/configure_camera_feed.html', {'form': form})
'''

# views.py
from django.shortcuts import render, redirect

def configure_camera_feed(request):
    if request.method == 'POST':
        # Get the URL from the form
        url = request.POST.get('feedLink')
        # Store the URL in the session
        request.session['camera_url'] = url
        return redirect('configure_camera_feed')  # Redirect to the same page
    else:
        # Get the stored URL from the session if available
        url = request.session.get('camera_url', '')
    return render(request, 'camera_config_app/configure_camera_feed.html', {'camera_url': url})
