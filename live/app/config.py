# Flask 설정 파일
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
    TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")

if not TURSO_DATABASE_URL and not TURSO_AUTH_TOKEN:
    # .env에 값이 있을 시에만 Turso를 사용하도록 설정
    SQLALCHEMY_DATABASE_URI = f"sqlite+{TURSO_DATABASE_URL}?secure=true"
    CONNECT_ARGS = {"auth_token": TURSO_AUTH_TOKEN}
else:
    # Turso 정보가 없거나 에러가 발생한다면 로컬 db를 사용하도록 설정
    print("\n[INFO] No Turso Setup: Use local db...\n")

    # instance 폴더 경로
    INSTANCE_DIR = os.path.join(os.path.dirname(__file__), "..", "instance")

    # 폴더가 없으면 생성 (해당 디렉토리가 기존에 존재하면 에러발생 없이 넘어가고, 없을 경우에만 생성)
    # False (default) -> exist_ok를 True로 설정하지 않았을 때 이미 해당 디렉토리가 존재하는 경우에는 exception에러
    os.makedirs(INSTANCE_DIR, exist_ok=True)

    SQLALCHEMY_DATABASE_URI = "sqlite:///instance/reviews.db"
    CONNECT_ARGS = {"check_same_thread": False}