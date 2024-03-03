from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)

camera = None

def generate_frames():
    global camera
    if camera is None:
        return
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed', methods=['POST'])
def video_feed():
    global camera
    if camera is None:
        rtsp_url = request.form['rtsp_url']
        camera = cv2.VideoCapture(rtsp_url)
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
