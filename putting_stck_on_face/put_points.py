import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import numpy as np
import cv2
import tensorflow as tf
from tqdm import tqdm
import argparse
import sys
from pathlib import Path
import io

""" Seeding """
np.random.seed(41)
tf.random.set_seed(41)

""" Function to plot landmarks on the image """
def plot_landmarks(image, landmarks):
    h, w, _ = image.shape
    
    for i in range(0, len(landmarks), 2):
        x = int(landmarks[i] * w)
        y = int(landmarks[i + 1] * h)
        image = cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
        num = int(i / 2 + 1)
        num_text = str(num)
        text_origin = (x, y + 10)
        TEXT_FACE = cv2.FONT_HERSHEY_DUPLEX
        TEXT_SCALE = 0.2
        TEXT_THICKNESS = 1
        image = cv2.putText(image, num_text, text_origin, TEXT_FACE, TEXT_SCALE, (0, 0, 255), TEXT_THICKNESS, cv2.LINE_AA)
    
    return image

def main(image_path, output_name):

    """ Hyperparameters """
    image_h = 512
    image_w = 512
    num_landmarks = 106
 

   # model_path = os.path.join("model", "model_mobile.h5") # Fixed model path

    model_path = "model/model_mobile.h5"

    print(model_path)
     
    output_directory = "result/"   # Fixed output directory



    """ Load the model """
    model = tf.keras.models.load_model(model_path)


    """ Reading the image """
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    image_x = image

    image = cv2.resize(image, (image_w, image_h))

    image = image / 255.0  ## (512, 512, 3)
    image = np.expand_dims(image, axis=0)  ## (1, 512, 512, 3)
    image = image.astype(np.float32)

    
    """ Prediction """
    pred = model.predict(image, verbose=0)[0]
    pred = pred.astype(np.float32)


    """ Saving the results """
    result_image = plot_landmarks(image_x.copy(), pred)

    # Determine the output path with the provided output name
    output_path = os.path.join(output_directory, f"{output_name}.png")

    cv2.imwrite(output_path, result_image)
    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict facial landmarks using a pre-trained model.")
    parser.add_argument("image_path", type=str, help="Path to the input image")
    parser.add_argument("output_name", type=str, help="Name of the output file (without extension)")

    args = parser.parse_args()
    main(args.image_path, args.output_name)