# import flask
# from flask import Flask,jsonify,render_template,request
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from keras.models import model_from_json
# import numpy as np
# import os
# import random
# import io
# from PIL import Image
# from werkzeug.utils import secure_filename
 
# ### Loadeng our model ###

# json_file = open('model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)
# loaded_model.load_weights("model.h5")
# print("Loaded model from disk")
 

# # loaded_model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate= 0.0001), metrics=['accuracy'])
# ### Class of Prediction ###


# def save_and_get_pred_img(image) :
#     defrance     = str(random.randint(1,100000))
#     curr_dir = os.path.abspath(os.path.dirname(__file__))
#     file         = "C:\\Users\\zeado\\Desktop\\final_proj\\predict" #change to eny dir
#     file_path    = os.path.join(file,defrance)
#     os.mkdir(file_path)
#     filename = secure_filename(image.filename)
#     next_file_path =os.path.join(file_path,defrance)
#     os.mkdir(next_file_path)
#     UPLOAD_FOLDER = next_file_path
#     my_wep_app.config['IMAGE_UPLOADS'] = UPLOAD_FOLDER
#     image.save(os.path.join(my_wep_app.config["IMAGE_UPLOADS"], image.filename))
#     return file_path 
 
# # class Api_service :

# #     def __init__(self,img_file_path):
# #         self.img_file_path = img_file_path

# #     def prediction_function(self) :
# #         data_generation = ImageDataGenerator(rescale=1.0/255)
# #         predict_generation = data_generation.flow_from_directory( self.img_file_path,target_size=(25,25),batch_size=10
# #                                                                 ,class_mode='categorical')

# #         prediction = loaded_model.predict_generator(predict_generation)
# #         has_cancer = 'The percentage of no cancer : '+ str(round(prediction[0][1]*100,2)) + "%"
# #         has_no_cancer='The Percentage of  cancer : ' + str(round(prediction[0][0]*100,2)) + '%'
# #         return has_cancer,has_no_cancer 

# # x = Api_service("C:\\Users\\zeado\\Desktop\\final_proj\\predict\\31733")
# # xx ,yy = x.prediction_function()
# # print(xx,yy) 
# # ### Creating our API & connected with HTML files ###
# # @my_wep_app.route("/")
# # def home():
# #     return render_template('index.html')
# # @my_wep_app.route("/result_page",methods=['GET', 'POST'])
# # def result_page():
# #    if request.method == "POST":

# #         if request.files:
# #             image = request.files["img"]
# #             img_file_path = save_and_get_pred_img(image)
# #             predict_img =Api_service(img_file_path)
# #             has_cancer,has_no_cancer = predict_img.prediction_function()
# #    return render_template("news-detail.html",has_cancer=has_cancer,has_no_cancer=has_no_cancer) 

# # my_wep_app.run(debug=True)

# app = Flask(__name__)

# @app.route('/', methods=["GET", "POST"])
# def home():
#     return render_template(r'index.html')

# @app.route("/result_page", methods=["POST"])
# def predict():
#     # initialize the data dictionary that will be returned from the
#     # view
#     data = {"success": False}

#     # ensure an image was properly uploaded to our endpoint
#     if flask.request.method == "POST":
#         if flask.request.files.get("image"):
#             # read the image in PIL format
#             image = flask.request.files["image"].read()
#             # image = Image.open(io.BytesIO(image))
#             # image = cv2.imread(total_data[6050].rstrip())

#             image_fromarray = Image.fromarray(image, 'RGB')
#             resize_image = image_fromarray.resize((224, 224))
#             expand_input = np.expand_dims(resize_image,axis=0)
#             input_data = np.array(expand_input)
#             input_data = input_data/255

#             pred = loaded_model.predict(input_data)
#             data["prediction"] = pred
#             print(pred)
#             if pred >= 0.5:
#                 data["class"] = 1
#                 data["class_str"] = "Cancer"
#                 print("1")
#             else:
#                 data["class"] = 0
#                 data["class_str"] = "No Cancer"
#                 print("0")

#     # return the data dictionary as a JSON response
#     return flask.jsonify(data)