from sqlalchemy import Column, Integer, String, Text
from . import Base

# TODO: Review 모델 클래스를 만드세요 (Base 상속)
# TODO: id, title, content, rating 컬럼을 정의하세요

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)   # 제목
    content = Column(Text, nullable=False)        # 리뷰 내용
    rating = Column(Integer, nullable=False)      # 별점 (1~5)

    # def __str__(self): # 출력, 프린트용 str(), print()
    # repr: 옵션이지만 많이들 사용하는 친구
    def __repr__(self): # 디버깅, 객체 프린트 예쁘게 하는 용도  # <__main__.User object at 0x102927770> -> <User(id=1, name='OO')>
        return f"<Reviews(id='{self.id}', title='{self.title}')>"
    
# class Board(db.Model):
#     __tablename__ = 'boards'