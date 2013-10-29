import datetime

last_id = 0

class Note:
    '''Represents a Note in the Notebook. Match against a string in searches and store tags for each note.'''
    def __init__(self, memo, tags=''):
        '''Initialize a note with memo and optional space separated tags. Autoset note creation_date and unique_id'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self,filter):
        '''Determine if this note matches the filter. Search is case sensitive and matches both text and tags'''
        return filter in self.memo or filter in self.tags

    
