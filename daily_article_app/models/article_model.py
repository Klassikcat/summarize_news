from daily_article_app import db
from daily_article_app.services.crawler import domain, get_domain_headlines, BASE_URL, get_one_article_text
from urllib.parse import parse_qs
from daily_article_app.models.summarize import summarize_txt
class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer(), primary_key=True)
    domain_name = db.Column(db.Text(), db.ForeignKey('domain_info.domain_name'))
    press_id = db.Column(db.Integer())
    title = db.Column(db.Text(), nullable=False)
    text = db.Column(db.Text)
    url = db.Column(db.Text())

    def __repr__(self):
        return f"Domain: {self.domain_id}"

def add_article(url):
    new_article = Article(
            id = url.split('&')[4].lstrip('aid='),
            domain_name = [key for key, value in domain.items() if [value] == parse_qs(url)['sid1']],
            press_id = parse_qs(url)['oid'],
            title = get_one_article_text(url)[0],
            text = summarize_txt(get_one_article_text(url)[1]),
            url = url.split('&')[4].lstrip('aid=')
            )
    if not db.session.query(Article).filter_by(title=new_article.title).first():
        db.session.add(new_article)
        db.session.commit()

def get_articles():
    return db.session.query(Article).all()

def get_one_article(target_name):
    return db.session.query(Article).filter_by(url=target_name).first()

def del_one_article(title):
    article_name = db.session.query(Article).filter_by(Article.title == title).first()
    db.session.delete(article_name)
    db.session.commit()

def del_all_article_domain(domain_id):
    domain_all = db.session.query(Article).filter_by(Article.domain_id == domain_id).all()
    db.session.delete(domain_all[i])
    db.session.commit()
