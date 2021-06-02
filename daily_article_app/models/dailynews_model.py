from daily_article_app import db
from daily_article_app.services import crawler

class Domain_info(db.Model):
    __tablename__ = 'domain_info'

    id = db.Column(db.Integer(), primary_key=True)
    domain_id = db.Column(db.Integer(), nullable=False)
    domain_name = db.Column(db.Text())
    article_rel = db.relationship('Article', backref='Article', cascade='all, delete')

    def __repr__(self):
        return f"분야: {self.domain_name}"

def add_domain(domain_id, domain_name):
    if domain_id.type() == int & domain_name.type() == str:
        new_domain = Domain_info(
                domain_id = domain_id,
                domain_name = domain_name
                )
        db.session(Domain_info)
        db.session.add(new_domain)
        db.session.commit()
    else:
        return "유효한 분야가 아닙니다"

def del_domain(domain_name):
     domain_del = Domain_info.query.filter(domain_name=domain_name)
     if domain_del:
        db.session.delete(domain_del)
        db.session.commit()

     def __repr__(self):
        return f"분야: {self.domain_name}"

def add_domain(domain_id, domain_name):
    if domain_id.type() == int & domain_name.type() == str:
        new_domain = Domain_info(
                domain_id = domain_id,
                domain_name = domain_name
                )
        db.session.add(new_domain)
        db.session.commit()
    else:
        return "유효한 분야가 아닙니다"

def del_domain(domain_name):
     domain_del = Domain_info.query.filter(domain_name=domain_name)
     if domain_del:
        db.session.delete(domain_del)
        db.session.commit()
