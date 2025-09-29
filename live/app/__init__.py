from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from .config import Config

'''
    create_engine
        데이터베이스를 연결 
    sessionmaker
        테이블 정의를 위한 세션 연결
'''
# TODO: DB 연결 엔진을 생성하세요 (create_engine)
# engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=True,
    connect_args=Config.CONNECT_ARGS
)

# TODO: 세션(SessionLocal) 객체를 만드세요 (scoped_session)
'''
    Session은 multi-thread간 thread-safe하지 않다
    그렇기에 하나의 스레드당 하나의 Session을 연결(thread.local, 스레드끼리 Session을 공유하지 않음) 
    -> 이것을 자동화 해주는 모듈이 scoped_session
'''
SessionLocal = scoped_session(sessionmaker(bind=engine,
                                            autocommit=False,   # 기본값 false
                                            autoflush=False    # autocommit과 함께 사용되며, 쿼리 실행 전에 변경사항이 자동으로 플러시(flush, DB로 전송)될지 여부를 결정
                                            ))
                                            
 
# TODO: Base 클래스를 만드세요 (declarative_base)
# 테이블을 정의하기 위한 기본설정. 
Base = declarative_base()

def create_app():
    """Flask 앱 생성 및 초기화"""
    app = Flask(__name__)

    # TODO: 모델을 import 하세요 (예: from . import models)
    from . import models

    # TODO: DB 테이블을 생성하세요 (Base.metadata.create_all)
    Base.metadata.create_all(bind=engine)

    # TODO: 라우트 블루프린트를 등록하세요 (review_routes 불러와서 app.register_blueprint)
    #  지연 로딩 또는 두 개 이상의 모듈이 서로를 임포트할 때 순환 참조 (Circular Reference) 문제가 발생할 수 있기에 함수 내부에 import
    from .routes.review_routes import review_bp
    # 라우트에서 설정한 블루프린트 객체를 플라스크 객체에 적용
    app.register_blueprint(review_bp)

    # 요청이 끝날 때마다 세션 닫기
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        SessionLocal.remove()

    return app
