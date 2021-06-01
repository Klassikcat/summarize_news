from flask import Blueprint, render_template, request
from daily_article_app.services.crawler import get_page, get_domain_headlines, get_articles, get_article_text, domain
from daily_article_app.models.article_model import get_articles
import textrankr

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/breaking' methods=['GET', 'POST'])
def breaking():
    msg_code = request.args.get('msg_code', None)
    alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None
    article_lists = get_articles()
    return render_template('breaking.html', alert_msg=alert_msg, user_list=user_list)

@bp.route('/domains')
def dom_summary():
    msg_code = request.args.get('msg_code', None)
    alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None
    article_lists = get_articles()
    return render_template('domains.html', alert_msg=alert_msg, user_list=user_list)


