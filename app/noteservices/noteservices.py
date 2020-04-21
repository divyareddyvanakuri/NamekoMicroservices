# http_service.py
import json
from nameko.rpc import rpc
from database import db_session
from models import Note

config = {'AMQP_URI':'amqp://guest:guest@localhost/'}

class HttpNoteService:
    name = "noteservice"
    
    @rpc
    def create_note(self, request,title,text,archive,color):
        note = Note(title,text,archive,color)
        db_session.add(note)
        db_session.commit()
        db_session.remove()
        return "successfully created the note"

    @rpc     
    def edit_note(self,id,title,text,archive,color):
        note = Note.query.get(id)
        if note:
            note.title = title
            note.text = text
            note.archive = archive
            note.color = color
            db_session.commit()
            db_session.remove()
            return "successfully updated the note"
        return "note not found"
    
    @rpc
    def delete_note(self,id):
        note = Note.query.get(id)
        if note:
            db_session.delete(note)
            db_session.commit()
            db_session.remove
            return "successfully deleted the note"
        return "note not found"
        
