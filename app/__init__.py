from flask import Flask
from .extensions import db, migrate, jwt, swagger_ui
from .logger import configure_logging
from .config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    configure_logging(app)
    
    from app.views.api import api_bp
    from app.views.admin import admin_bp
    
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    app.register_blueprint(swagger_ui, url_prefix='/api/docs')
    
    @app.route('/api/spec')
    def api_spec():
        with open('docs/api.yaml') as f:
            return f.read()
    
    with app.app_context():
        db.create_all()
        try:
            from app.services.auth import create_admin_user
            create_admin_user()
        except Exception as e:
            app.logger.warning(f"Could not create admin user: {str(e)}")
    
    return app