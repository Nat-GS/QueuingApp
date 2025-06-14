import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://postgres:123456@db.utmshjkhipwtbdbeaxpe.supabase.co:5432/postgres') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '123456'



