class Score_database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    math_score = db.Column(db.Float)
    chinese_score = db.Column(db.Float)
    total_score = db.Column(db.Float)