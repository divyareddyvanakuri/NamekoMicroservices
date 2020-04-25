# rpc_service.py
import json
from nameko.rpc import rpc
from models import Note,Label,Association,save,delete,update

config = {'AMQP_URI':'amqp://guest:guest@localhost/'}

class NoteService:
    name = "noteservices"
    
    @rpc
    def create_note(self,userid,title,text,archive,color,labelname):
        if userid == None:
            return json.dumps({'error':'please login','status':400})
        archive = bool(archive)
        note = Note(title,text,archive,color,userid)
        save(note)
        noteid = note.id
        print(noteid)
        association = Association(noteid,labelname)
        save(association)
        return json.dumps({'success':"successfully created the note",'status':201})

    @rpc     
    def edit_note(self,id,userid,title,text,archive,color):
        note = Note.query.get(id)
        if note.userid == userid:
            note.title = title
            note.text = text
            note.archive = bool(archive)
            note.color = color
            update()
            return json.dumps({'success':"successfully updated the note",'status':202})
        return json.dumps({'error':'unauthorized user','status':401})
    
    @rpc
    def delete_note(self,id,userid):
        note = Note.query.get(id)
        if note.userid == userid:
            association = Association.query.filter_by(noteid=id).first()
            delete(association)
            delete(note)
            return json.dumps({'success':"successfully deleted the note",'status':200})
        return json.dumps({'error':'unauthorized user','status':401})

    @rpc    
    def create_label(self,userid,labelname):
        if userid == None:
            return json.dumps({'error':'please login','status':400})
        label = Label(labelname,userid)
        save(label)
        return json.dumps({'success':"successfully created the label",'status':201})
    
    @rpc
    def delete_label(self,userid,labelname):
        if userid == None:
            return json.dumps({'error':'please login','status':400})
        association = Association.query.filter_by(labelname=labelname)
        delete(association)
        label = Label.query.filter_by(labelname=labelname).first()
        delete(label)