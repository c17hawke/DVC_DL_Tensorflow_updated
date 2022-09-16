import tensorflow as tf
from pathlib import Path
import streamlit as st
from PIL import Image
import numpy as np
import os


# @st.cache()
def load_model(path: Path=Path("./model.h5")) -> tf.keras.models.Model:
    if os.path.exists(path):
        model = tf.keras.models.load_model(path)
        return model
    else:
        raise FileNotFoundError("model file not found")

def prediction(img, model, label_map={1: "dog", 0: "cat"}):
    original_img = Image.open(img)
    img = np.array(original_img)
    img = tf.expand_dims((tf.image.resize(img, (224, 224))), axis=0)
    result = model.predict(img)
    idx = np.argmax(result, axis=1)[0]
    pred_class = label_map[idx]
    return original_img, pred_class


if __name__ == "__main__":
    try:
        st.title("examples")
        st.title('Welcome To Project!')
        instructions = """
            Just upload an image
            """
        st.write(instructions)
        file = st.file_uploader("upload an image", type=["jpg"])

        model = load_model()
        if file:
            original_img, response = prediction(file, model)

            st.title("Here is the image you've selected")
            st.image(original_img)
            st.title(f"result: {response}")

    except Exception as e:
        raise e