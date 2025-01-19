from db import db

class ItemModel(db.Model):
    __tablename__ ="items" #nome tabella per gli oggetti di questa classe
    #definire le colonne
    id=db.Column(db.Integer,primary_key=True) #Di default si autoincrementa
    name=db.Column(db.String(80),unique=False,nullable=False)#unique=True se si vuole che un oggetto sia unico per TUTTI i negozi
    description=db.Column(db.String)
    price=db.Column(db.Float(precision=2),unique=False,nullable=False)
    store_id=db.Column(db.Integer,db.ForeignKey("stores.id"),unique=False,nullable=False)
    store=db.relationship("StoreModel",back_populates="items")#back_populates permette di fare il collegamento bidirezionale tra le due tabelle
    tags=db.relationship("TagModel",back_populates="items",secondary="items_tags")

