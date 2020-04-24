# http_service.py
import json
from nameko.rpc import rpc
from models import Note

config = {'AMQP_URI':'amqp://guest:guest@localhost/'}

class NoteService:
    name = "noteservices"
    
    @rpc
    def create_note(self,userid,title,text,archive,color):
        if userid == None:
            return json.dumps({'error':'please login','status':400})
        archive = bool(archive)
        note = Note(title,text,archive,color,userid)
        note.save(note)
        return json.dumps({'success':"successfully created the note",'status':201})

    @rpc     
    def edit_note(self,id,userid,title,text,archive,color):
        note = Note.query.get(id)
        if note.userid == userid:
            note.title = title
            note.text = text
            note.archive = bool(archive)
            note.color = color
            note.update()
            return json.dumps({'success':"successfully updated the note",'status':202})
        return json.dumps({'error':'unauthorized user','status':401})
    
    @rpc
    def delete_note(self,id,userid):
        note = Note.query.get(id)
        if note.userid == userid:
            note.delete(note)
            return json.dumps({'success':"successfully deleted the note",'status':200})
        return json.dumps({'error':'unauthorized user','status':401})
        
