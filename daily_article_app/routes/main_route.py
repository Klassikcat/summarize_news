from flask import Blueprint,render_template, request
from daily_article_app.services.crawler import get_page, get_domain_headlines, get_articles, get_article_text, domain
from daily_article_app.models import article_model
from daily_article_app.models.summarize import summarize_txt
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    headlines_url = get_domain_headlines('속보')
    press_id_col, press_name_col, article_url_col = get_articles(headlines_url, 19)
    breaking_news_title = []
    breaking_news_texts = []
    for i in range(9):
        press_ids = press_id_col[i]
        article_urls = article_url_col[i]
        article_title, article_text = get_article_text(headlines_url, press_ids, article_urls)
        article_text = summarize_txt(article_text, 3)
        breaking_news_title.append(article_title)
        breaking_news_texts.append(article_text)
    return render_template("index.html", titles=breaking_news_title, texts=breaking_news_texts, press_ids=press_id_col, press_names=press_name_col, article_urls=article_url_col)

@bp.route('/articles', methods=['GET', 'POST'])
def article_summary():
    msg_code = request.args.get('msg_code', None)
    alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None
    get_all = article_model.get_articles() 
    return render_template('articles.html', alert_msg=alert_msg, get_all=get_all)
