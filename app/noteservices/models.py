class Note(object):
   
    def __init__(self, title=None, text=None, archive=None, color=None,userid=None):
        self.title = title
        self.text = text
        self.archive = archive
        self.color = color
        self.userid = userid
    def __repr__(self):
        return '<Note %r>' % (self.title)


