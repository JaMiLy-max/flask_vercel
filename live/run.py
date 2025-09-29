# Flask 앱 만들고 실행
from app import create_app

# Flask 앱 생성
app = create_app()

# 파이썬에서 "직접 실행했을 때"만 실행되는 부분
if __name__ == "__main__":
    # Flask 개발 서버 실행
    # debug=True → 코드 저장 시 자동으로 서버 재시작 + 에러 화면을 자세히 보여줌
    app.run(debug=True)
