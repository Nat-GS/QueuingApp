from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import datetime
from flask import current_app

class UsuarioService:

    @staticmethod
    def login(email, contrasenia): 
        usuario = UsuarioRepository.get_usuario_by_email(email)

        if not usuario:
            return {"error": "Usuario no encontrado"}, 404

        if usuario.contrasenia != contrasenia:
            return {"error": "Contraseña incorrecta"}, 401

        try:
            token = jwt.encode({
                'usuario_id': usuario.id_usuario,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }, current_app.config.get('SECRET_KEY', 'default_secret'), algorithm='HS256')

            if isinstance(token, bytes):
                token = token.decode('utf-8')  # Asegurar que sea string en Flask

        except Exception as e:
            return {"error": f"Error generando token: {str(e)}"}, 500


        return {
            "id_usuario": usuario.id_usuario,
            "nombre": usuario.nombre,
            "token": token,
            "hospital_id": usuario.hospital_id
        }, 200

    @staticmethod
    def create_usuario(data):
        nuevo_usuario = Usuario(
            nombre=data.get('nombre'),
            email=data.get('email'),
            telefono=data.get('telefono'),
            contrasenia=data.get('contrasenia'),
            hospital_id=data.get('hospital_id')  # si es necesario
        )

        return UsuarioRepository.add_usuario(nuevo_usuario)
