from flask import Flask, jsonify, send_from_directory, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)  # ✅ Definir app primero

    # Configuración de la app
    CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}}, supports_credentials=True)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import Usuario, Queue, Hospital
    from app.routes import register_routes

    register_routes(app)

    # ✅ Ruta base para evitar 404
    @app.route('/')
    def index():
        return jsonify({"message": "Servidor activo"}), 200

    # ✅ Ruta para servir archivos
    @app.route('/app/output/<folder>/<filename>')
    def serve_output_file(folder, filename):
        valid_folders = ['csv', 'simulations']
        if folder not in valid_folders:
            return abort(404)

        directory = os.path.abspath(os.path.join('app', 'output', folder))
        file_path = os.path.join(directory, filename)

        if not os.path.exists(file_path):
            return f"Archivo no encontrado: {file_path}", 404

        return send_from_directory(directory, filename, as_attachment=True)

    return app
