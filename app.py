from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

def generate_frames():
    camera = cv2.VideoCapture('rtsp://admin:admin@123@172.16.21.100:554/cam/realmonitor?channel=5&subtype=0&unicast=true&proto=Onvif')
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
