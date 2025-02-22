import bcrypt
from app import db
from .base import BaseModel

class User(BaseModel):    
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.LargeBinary(60), nullable=False)  # Store as binary for bcrypt
    blogs = db.relationship('Blog', back_populates='user')
    
    def set_password(self, password):
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

    def check_password(self, password):
        # Check hashed password
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)


