from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_redis import FlaskRedis
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
redis_client = FlaskRedis()

swagger_ui = get_swaggerui_blueprint(
    '/api/docs',
    '/api/spec',
    config={'app_name': "Exam API"}
)