from pathlib import Path


def main():
    my_path = Path()
    # 뭔지 모르겠지만 출력해보니 현재 경로를 출력함
    print("나의 현재경로 : ", my_path.resolve())
    print(my_path.resolve().parent)
    print(my_path.resolve().parent.parent)
    print(my_path.resolve().parent.parent.parent)

if __name__ == '__main__':
    main()