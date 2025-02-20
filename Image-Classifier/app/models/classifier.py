import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from app.config import settings

class ImageClassifier:
    def __init__(self):
        self.model = self._build_model()
    
    def _build_model(self):
        base_model = ResNet50(weights="imagenet", include_top=False)
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(1024, activation="relu")(x)
        predictions = Dense(1, activation="sigmoid")(x)
        model = Model(inputs=base_model.input, outputs=predictions)
        model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
        return model
    
    def load_model(self):
        self.model = tf.keras.models.load_model(settings.MODEL_PATH)
    
    def predict(self, image):
        image = image.resize((224, 224))
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = tf.keras.applications.resnet50.preprocess_input(image)
        prediction = self.model.predict(image)
        return prediction[0][0]