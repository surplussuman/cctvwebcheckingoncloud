'''
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
'''

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
'''
import cv2
from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
from django.views.decorators import gzip

camera = None
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

@gzip.gzip_page
def video_feed(request):
    global camera
    if request.method == 'POST':
        rtsp_url = request.POST.get('rtsp_url')
        camera = cv2.VideoCapture(rtsp_url)

    if camera is None:
        return render(request, 'camera_config_app/index.html')

    def generate():
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')


