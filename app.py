from flask import Flask, render_template, request
import cv2
from PIL import Image


app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html

@app.route('/image')
def load():
    data = []
    for number in range(100):
        num = str(number) + '.jpg'
        data.append(num)
    return render_template('loadimage.html',data=data)

@app.route('/convert', methods=['GET', 'POST'])
def convert_image():
    path_hasil = 'static/assets/hasil/'
    if request.method == 'POST':
        file = request.files['query_img']
        img = Image.open(file.stream)  # PIL image
        uploaded_img_path = 'static/assets/upload/'+ file.filename
        result_name = file.filename[:-4]
        img.save(uploaded_img_path)
        img_input = cv2.imread(uploaded_img_path)
        gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(path_hasil + result_name +'.jpg', gray)
        return render_template('convert.html',query_path=uploaded_img_path,img=result_name)
    else:
        return render_template('convert.html')
    


if __name__ == '__main__':
    app.run(debug=True)