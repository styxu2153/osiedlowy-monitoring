from app import app, db

class Flaga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    discord_name = db.Column(db.String(32), index = True)
    domain_name = db.Column(db.String(32), index = True, unique=True)
    status = db.Column(db.String(24), default="")
    
    def __repr__(self):
        return f'<Discord Name {self.discord_name}>'