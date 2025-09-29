"""
서비스 계층 (Service Layer)
- 라우트에서 직접 DB 조작하지 않고
- 이 모듈을 거쳐서 DB CRUD 실행

 * ORM 방식은 객체지향적으로 접근하며 모델 인스턴스를 수정하고 commit() 합니다.
 * SQL Expression 방식은 SQL 스타일로 업데이트 쿼리를 작성하여 좀 더 명시적으로 SQL 업데이트 작업을 수행할 수 있습니다.
"""

from app import SessionLocal
from app.models import Review


def get_all_reviews():
    """모든 리뷰 조회"""
    db = SessionLocal()
    return db.query(Review).all()


def create_review(title, content, rating):
    """리뷰 생성"""
    db = SessionLocal()
    review = Review(title=title,content=content,rating=rating)
    db.add(review)
    db.commit()
    return review


def get_review_by_id(review_id):
    """ID로 리뷰 조회"""
    # get() 메서드는 오직 해당 모델(Review)의 **기본 키 (Primary Key)**를 기준으로 객체를 조회하도록 설계
    db = SessionLocal()
    return db.query(Review).get(review_id)


def update_review(review_id, title, content, rating):
    """리뷰 수정"""
    db = SessionLocal()
    review = db.query(Review).get(review_id)
    if review:
        review.title = title
        review.content = content
        review.rating = rating
        db.commit()
    return review


def delete_review(review_id):
    """리뷰 삭제"""
    db = SessionLocal()
    review = db.query(Review).get(review_id)
    if review:
        db.delete(review)
        db.commit()
