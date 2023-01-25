from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()

# class to connect this app with a database
class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1500), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.text}"

@app.route('/')
def index():
    return 'Sub-Task 2'

# view
@app.route('/api/note/<id>', methods=["GET"])
def get_note(id):
    note = Notes.query.get_or_404(id)
    return {"id": note.id, "description": note.text}

# create
@app.route('/api/note', methods=['POST'])
def add_note():
    note = Notes(id=request.json['id'], text=request.json['text'])
    db.session.add(note)
    db.session.commit()
    return {'id': note.id}

# delete
@app.route('/api/note/<id>', methods=['DELETE'])
def delete_note(id):
    note = Notes.query.get(id)
    if note is None:
        return {"error": "not found"}
    db.session.delete(note)
    db.session.commit()
    return {"message": "done!"}

# update
@app.route('api/note/<id>', methods=["PUT"])
def update_note(id):
    note = Notes.query.get(id)
    note.text = "new-text"
    return "updated"