# pip install pillow
from PIL.Image import Image
# pip install numpy
import numpy as np

import tensorflow as tf

# model_loader.py
from model_loader import model

# 타입 명시: Image 타입의 매개변수 image가 쓰일 것
def predict(image: Image):
    
    # 모델에 넘겨줄 input 이미지 조정
    # 이미지 사이즈 224x224 로 조정
    # 이미지 객체를 Numpy 배열로 변경
    # :3 - RGB를 의미함
    image = np.asarray(image.resize((224, 224)))[..., :3]

    # 차원을 확장
    image = np.expand_dims(image, 0)

    # 정확도를 높이기 위해 정규화
    # image pixel 범위: 0~225 > 그 반값 127.5 
    image = image / 127.5 - 1.0

    # 결과값 수
    count = 3

    results = tf.keras.applications.imagenet_utils.decode_predictions(
        model.predict(image), count
    )[0]

    print(results)


    # API 생성 - { 'key': 'value', ... } dict 로 반환
    result_list = []
    for i in results:
        result_list.append({
            # 클래스 네임
            'class': i[1],
            # 정확도 - 소수 둘째자리까지 % 수치로 반환
            'confidence': f'{i[2]*100:0.2f}'
        })
    
    return result_list
