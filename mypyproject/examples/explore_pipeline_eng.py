from transformers import pipeline
# 파이토치 설치해야 함
from sys import stdout
import logging
logging.basicConfig(stream=stdout, level=logging.INFO)


def main():
    # 만들고 싶었던 것의 간단한 프로토타입을 구현.
    # 파이프 라인을 통해 올려놓은 최신 모델들을 써볼 수있음. 다운로드 시작
    # 이걸 실행하면 사전훈련된 모델들을 다운로드해줌
    # 분류기를 가져오는 것 같고?
    classifier = pipeline("sentiment-analysis")
    # classifier -> __call__ (문장) -> list -> 첫번째 -> 결과
    result = classifier("I hate you")[0]
    print(result)
    # 한글은 학습을 하지 않은 감성분석 모델.
    result = classifier("나는 널 싫어해")[0]
    print(result)
    # 비꼬는 말에 대응? - saracasm에는 대응하지 못한다.
    result = classifier("Well, what a surprise.")[0]
    print(result)


if __name__ == '__main__':
    main()