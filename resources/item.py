from flask.views import MethodView
from flask_smorest import Blueprint,abort
from flask_jwt_extended import jwt_required,get_jwt
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemUpdateSchema,ItemSchema

blp= Blueprint("items", __name__, description="Operations on items")

@blp.route("/item/<int:item_id>")
class Item(MethodView):
    @jwt_required()
    @blp.response(200,ItemSchema)#perchè invia come return un qualcosa 
    def get(self,item_id):
        item= ItemModel.query.get_or_404(item_id)#restituisce l'item dalla sua chiave primaria e fa un errore 404 se non lo trova
        return item

    @jwt_required()
    def delete(self,item_id):
        jwt=get_jwt()
        if not jwt.get("admin"):
            abort(401,message="User is not an admin.")
        #lo fa solo se utente è admin(id=='1')
        item= ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message":"Item deleted"}
    
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200,ItemSchema)
    def put(self,item_data,item_id):#item data va per secondo , è il body del messaggio
        item= ItemModel.query.get(item_id)
        if item:#se esiste non serve store id(ovviamente esso può essere mandato ma verrà ignorato)
            item.price=item_data["price"]
            item.name=item_data["name"]    
        else:#non esiste e lo crea prendendo anche store id,sarà null se quel negozio non esiste
            item=ItemModel(id=item_id,**item_data)

        db.session.add(item)
        db.session.commit()
        
        return item

@blp.route("/item")
class ItemList(MethodView):
    @jwt_required()
    @blp.response(200,ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
    
    @jwt_required(fresh=True)#serve avere un token di accesso jwt per eseguire questo endpoint,il jwt va nel header della richiesta,fresh=true significa che dev'essere un jwt fresco
    @blp.arguments(ItemSchema)
    @blp.response(201,ItemSchema)
    def post(self,item_data):
        item=ItemModel(**item_data)#prende i dati dalla richiesta post e rende il dizionario dei kwargs per riempire ItemModel

        try:
            db.session.add(item)#inserisce nel database quando si fa commit()
            db.session.commit()
        except SQLAlchemyError:
            abort(500,message="An error occured while inserting the item")
        
        
        return item,201

