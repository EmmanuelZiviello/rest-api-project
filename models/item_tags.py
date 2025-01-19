from db import db

#classe che rappresenta la tabella tra tag e item perchè è una relazione N:N
class ItemTags(db.Model):
    __tablename__ ="items_tags"

    id=db.Column(db.Integer,primary_key=True)
    #legame tra le tabelle
    item_id=db.Column(db.Integer,db.ForeignKey("items.id"))
    tag_id=db.Column(db.Integer,db.ForeignKey("tags.id"))
