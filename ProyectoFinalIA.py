!pip install opencv-python
!pip install mtcnn


drive.mount('/content/drive')
import sys
sys.path.append('/content/drive/My Drive/IA/ProyectoFinalIA/')


!pip install mtcnn
from mtcnn import MTCNN
import numpy as np
import tensorflow as tf
import tensorflow.keras
import torch
import timeit
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from google.colab import drive
from utils.bounding_box import resizeBoundingBox
from utils.predictor_keras import predict
from utils.detect_faces import detect_faces, detect_faces_with_mask


IMG_WIDTH = 160 # Ancho de la imagen
IMG_HEIGHT = 160 # Alto de la imagen
BBOX_PERCENTAGE = 0.05 # Porcentage de ampliación del bounding box
CONFIDENCE = 0.80 # Porcentage de confidencia del detector de rostros
classes = ['no_mask', 'mask'] # Clases de la capa final


img = cv2.imread('/content/drive/My Drive/IA/ProyectoFinalIA/multimedia/test3.jpg')
img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 10))
plt.title("Imagen original")
plt.imshow(img_color)
plt.show()


# Detector de rostros (Multi-Task Cascaded Convolutional Neural Network)
face_detector = MTCNN()


# Verificamos la detección de rostros
image_detected = detect_faces(img_color, face_detector, confidence=CONFIDENCE, target_size=(IMG_WIDTH, IMG_HEIGHT))
plt.figure(figsize=(12, 12))
plt.title('Detección de Rostros')
plt.imshow(image_detected)
plt.show()


# Probamos sobre otra imagen
img_test = cv2.imread('/content/drive/My Drive/IA/ProyectoFinalIA/multimedia/test4.jpg')
img_color_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
image_detected2 = detect_faces(img_color_test, face_detector, confidence=CONFIDENCE, target_size=(IMG_WIDTH, IMG_HEIGHT))
plt.figure(figsize=(12, 12))
plt.title('Detección de Rostros')
plt.imshow(image_detected2)
plt.show()


# Detector de mascaras (MaskNet)
model_keras = tf.keras.models.load_model('/content/drive/My Drive/IA/ProyectoFinalIA/models/mask_net.hdf5')


image_mask_detection = detect_faces_with_mask(img_color, face_detector, model_keras, classes, 
                                   CONFIDENCE, bbox_percentage=BBOX_PERCENTAGE, predictor='keras', 
                                   target_size=(IMG_WIDTH, IMG_HEIGHT))

plt.figure(figsize=(12, 12))
plt.imshow(image_mask_detection)
plt.show()

# Probamos sobre otra imagen
img_test = cv2.imread('/content/drive/My Drive/IA/ProyectoFinalIA/multimedia/test5.jpg')
img_color_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
image_mask_detection = detect_faces_with_mask(img_color_test, face_detector, model_keras, classes, 
                                   CONFIDENCE, bbox_percentage=BBOX_PERCENTAGE, predictor='keras', 
                                   target_size=(IMG_WIDTH, IMG_HEIGHT))

plt.figure(figsize=(12, 12))
plt.imshow(image_mask_detection)
plt.show()

model_torch = torch.load('/content/drive/My Drive/IA/ProyectoFinalIA/models/best_model_conv_ft2.model')

image_mask_detection = detect_faces_with_mask(img_color, face_detector, model_torch, ['mask', 'no_mask'], 
                                              CONFIDENCE, bbox_percentage=BBOX_PERCENTAGE, predictor='torch', 
                                              target_size=(IMG_WIDTH, IMG_HEIGHT))

plt.figure(figsize=(12, 12))
plt.imshow(image_mask_detection)
plt.show()

# Probamos sobre otra imagen
img_test = cv2.imread('/content/drive/My Drive/IA/ProyectoFinalIA/multimedia/test5.jpg')
img_color = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
image_mask_detection = detect_faces_with_mask(img_color, face_detector, model_torch, ['mask', 'no_mask'], 
                                              CONFIDENCE, bbox_percentage=0.07, predictor='torch', 
                                              target_size=(IMG_WIDTH, IMG_HEIGHT))

plt.figure(figsize=(12, 12))
plt.imshow(image_mask_detection)
plt.show()

# Probamos sobre otra imagen
img_test = cv2.imread('/content/drive/My Drive/IA/ProyectoFinalIA/multimedia/test3.jpg')
img_color = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
image_mask_detection = detect_faces_with_mask(img_color, face_detector, model_torch, ['mask', 'no_mask'], 
                                              CONFIDENCE, bbox_percentage=0.07, predictor='torch', 
                                              target_size=(IMG_WIDTH, IMG_HEIGHT))

plt.figure(figsize=(12, 12))
plt.imshow(image_mask_detection)
plt.show()