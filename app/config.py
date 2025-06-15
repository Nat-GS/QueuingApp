import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://admin:x4RInidnXfZHHxdMF5JDKlbHwhFzr20W@dpg-d1721a8dl3ps739v12hg-a.oregon-postgres.render.com/modelado_qy8z') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '123456'



