from flask import Blueprint, request, redirect, url_for, Response
from daily_article_app.services import crawler
from daily_article_app.models import article_model, dailynews_model
from urllib.parse import parse_qs
from daily_article_app import db

bp = Blueprint('article', __name__)

@bp.route('/article', methods=['GET', 'POST'])
def add_news():
    db.create_all()
    article_new = request.form.get('url_submit')
    try:
        raw_article = crawler.get_one_article_text(url) 
        if not url:
            return "url이 필요합니다."
        elif article_model.get_one_article(target_name=url) == None:
            article_model.add_article(url)
            domain_id = parse_qs(url)
            dailynews_model.add_domain(domain_id=domain_id['sid1'], domain_name=[key for key, value in crawler.domain.items() if value == [domain_id['sid1']][0]])
            return redirect(url_for('main.article_summary'))
        else:
            return redirect(url_for('main.article_summary'))
    except:
            return redirect(url_for('main.article_summary'))

@bp.route('/article/<string:title>', methods=['GET', 'POST'])
def del_news():
    db.create_all()
    if title == None:
        return "삭제할 뉴스의 제목을 입력하세요"
    elif Article.query.filter(Article.title == title).first() == None:
        return "해당 뉴스가 없습니다"
    else:
        article_model.del_one_article(title)
        return redirect(url_for('main.article_summary'))

