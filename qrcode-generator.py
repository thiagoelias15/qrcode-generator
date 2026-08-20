from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/', methods = ['GET'])

def home():
    return render_template('index.html', qr_image = None)

@app.route('/generate', methods = ['POST'])

def generar_qr():
    
    website_link = request.form.get('link')
    
    if not website_link:
        return "URL Not Provided", 400
    
    qr = qrcode.make(website_link)
    buffer = io.BytesIO()
    qr.save(buffer, format = "PNG")
    
    img_bytes = base64.b64encode(buffer.getvalue())
    img_string = img_bytes.decode('utf-8')
    
    return render_template('index.html', qr_image = img_string, last_link = website_link)

if __name__ == '__main__':
    print("Server up. Open your browser on: http://localhost:5000")
    app.run(debug=True)