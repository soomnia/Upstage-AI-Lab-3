# tensorflow에서 img 모델 로드 > 이미지 데이터 넘기기 > 결과값 출력
# pip install tensorflow
import tensorflow as tf

def load_model():
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    print("Success to load model")

    return model

model = load_model()