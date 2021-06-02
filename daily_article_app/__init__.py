from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    daily_article_app = Flask(__name__)

    if daily_article_app.config["ENV"] == 'production':
        daily_article_app.config.from_object('config.ProductionConfig')
    else:
        daily_article_app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        daily_article_app.config.update(config)

    db.init_app(daily_article_app)
    migrate.init_app(daily_article_app, db)

    from daily_article_app.routes import (main_route, article_route)
    daily_article_app.register_blueprint(main_route.bp)
    daily_article_app.register_blueprint(article_route.bp, url_prefix='/api')

    return daily_article_app

if __name__ == "__main__":
    daily_flask_app = create_app()
    daily_article_app.run(debug=True)


