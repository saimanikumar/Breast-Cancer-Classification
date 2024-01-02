import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow
from keras.models import model_from_json
from PIL import Image
import cv2
from werkzeug.utils import secure_filename
import numpy as np
from flask import Flask, render_template, request



### Loadeng model ###
json_file = open(
    r'C:\Users\D. Sai Mani Kumar\Downloads\BreasCancerResnet(86%)\model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(
    r"C:\Users\D. Sai Mani Kumar\Downloads\BreasCancerResnet(86%)\model.h5")
print("Loaded model from disk")


def save_and_get_pred_img(image):

    file = r"C:\Users\D. Sai Mani Kumar\Downloads\BreasCancerResnet(86%)\static"
    filename = secure_filename(image.filename)

    UPLOAD_FOLDER = file

    app.config['IMAGE_UPLOADS'] = UPLOAD_FOLDER
    image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

    file_total_path = os.path.join(file, filename)
    print(file_total_path)

    return file_total_path


class Api_service:

    def __init__(self, img_file_path):
        self.img_file_path = img_file_path

    def prediction_function(self):
        model_path = r"./model.h5"
        loaded_model = tensorflow.keras.models.load_model(model_path)

        image = cv2.imread(self.img_file_path)

        image_fromarray = Image.fromarray(image, 'RGB')
        resize_image = image_fromarray.resize((224, 224))
        expand_input = np.expand_dims(resize_image, axis=0)
        input_data = np.array(expand_input)
        input_data = input_data/255

        pred = loaded_model.predict(input_data)

        x = pred[[0]]
        class1_prob = x


        has_cancer = False

        if pred >= 0.5:
            has_cancer = True
            print("1")
        else:
            has_cancer = False
            print("0")

        return has_cancer


## Creating our API & connected with HTML files ###
app = Flask(__name__)


@app.route("/")
def home():
    return render_template(r"index.html")


@app.route("/result_page", methods=['GET', 'POST'])
def result_page():
    if request.method == "POST":
        if request.files:

            image = request.files["img"]
            img_file_path = save_and_get_pred_img(image)

            predict_img = Api_service(img_file_path)
            has_cancer = predict_img.prediction_function()

            print(has_cancer)

    return render_template(r"result.html", has_cancer=has_cancer)


app.run(debug=True)
