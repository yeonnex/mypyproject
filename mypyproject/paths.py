# 프로젝트의 디렉토리를 설정
# 물론 아래처럼 하드코딩할수도 있겠지만, 나중에 클론했을 떄 컴퓨터가 다르기 떄문에 안되는 현상이 발생한다
from pathlib import Path
from os import path

ROOT_DIR_BAD = 'C:/Users/yeonn/Desktop/Projects/Toy/mypyproject/mypyproject/examples'
# 그러니, 루트 디렉토리 구할 떄 이렇게 하드코딩하지 말자.

# 이렇게 하자!
# 프로젝트의 디렉토리를 설정

ROOT_DIR = Path().resolve().parent.parent.__str__()
# 이렇게 미리 경로를 선언해주면, 나중에 이 상수를 임포트만 해서 사용할 수 있습니다.
TEXT_PATH = path.join(ROOT_DIR, "data", "text.txt")
