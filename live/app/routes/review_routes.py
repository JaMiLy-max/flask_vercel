"""
라우트 (Controller Layer)
- 사용자가 요청한 URL을 처리하고
- 서비스 계층을 호출해서 DB 조작
- 결과를 템플릿에 전달
"""

from flask import Blueprint, render_template, request, redirect, url_for
from app.services.review_service import (
        get_all_reviews, create_review, get_review_by_id,
        update_review, delete_review
)

# 블루프린트 생성
review_bp = Blueprint("review", __name__)

@review_bp.route("/")
def index():
    """리뷰 목록 + 평균 별점"""
    reviews = get_all_reviews()
    # 평점의 평균 첫째자리까지 반올림. 없으면 0
    avg = round(sum([r.rating for r in reviews]) / len(reviews), 1) if reviews else 0
    return render_template("index.html", reviews=reviews, avg_rating=avg)


@review_bp.route("/new", methods=["GET", "POST"])
def new_review():
    """새 리뷰 작성"""
    '''
    SQLAlchemy 자체에는 웹 리디렉션을 수행하는 기능이 내장되어 있지 않다.
    SQLAlchemy는 Python의 데이터베이스 툴킷이자 ORM(Object-Relational Mapping) 라이브러리이므로
    일반적으로 Flask나 Django와 같은 웹 프레임워크와 함께 사용한다. 
    그러므로 리디렉션이 필요하다면 사용하는 웹 프레임워크에서 제공하는 redirect함수를 사용해야한다.
    '''
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        rating = int(request.form["rating"])
        create_review(title, content, rating)
        # redirect : 데이터베이스 작업이 성공적으로 완료된 후, 사용자를 특정 URL로 이동시키는 Flask의 기능
        # url_for : 동적으로 URL을 생성. 블루프린트(Blueprint)를 통해서 index 뷰 함수를 찾음.(Endpoint)
        return redirect(url_for("review.index"))
    # 빈 new.html page
    return render_template("new.html")


@review_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_review(id):
    """리뷰 수정"""
    review = get_review_by_id(id)
    if request.method=="POST":
        title = request.form["title"]
        content = request.form["content"]
        rating = int(request.form["rating"])
        update_review(id, title, content, rating)
        return redirect(url_for("review.index"))
    return render_template("edit.html", review=review)


@review_bp.route("/delete/<int:id>")
def delete_review_route(id):
    """리뷰 삭제"""
    delete_review(id)
    return redirect(url_for("review.index"))
