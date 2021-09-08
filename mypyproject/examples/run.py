from mypyproject.paths import TEXT_PATH
def main():
    with open(TEXT_PATH, 'r',encoding='UTF-8') as fh:
        text = fh.read()
    print(text)
# 이렇게 하면, 굳이 경로를 또 입력하지 않아도
# 미리 코딩되어있는 경로를 찾아와서 파일을 읽기 때문에
# 매우 편리하다!
# '안녕!' 이라는 텍스트가 잘 출력되는 것을 볼 수 있다.
if __name__ == '__main__':
    main()

