from mongoengine import connect, Document, StringField, DateTimeField, GeoJsonBaseField
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime
import json
app = FastAPI()
from typing import Dict, Any
connect('securedata', host="mongodb+srv://sahiljoya11:sahil1122@cluster0.syubkoh.mongodb.net/securedata")

class DataModel(Document):
    appname= StringField(required=True, max_length=200)
    datajson = StringField(required=True,)
    clientName = StringField(required=True, max_length=200)
    created = StringField(default=f"{datetime.date.today()}")
class Contact(Document):
    name = StringField(required=True)
    number = StringField(required=True)
    email = StringField()
    

class DataRequest(BaseModel):
    appname: str
    datajson: str
    clientName: str
    
@app.post("/api/v1/create-data")
async def createData(dataModel: DataRequest):
    findData = DataModel.objects(clientName=dataModel.clientName).first()
    if findData:
        findData.delete()
        data = DataModel(appname=dataModel.appname, datajson=str(dataModel.datajson), clientName=dataModel.clientName)
        data = data.save()
        return {
            "message":"Thank tou bro 😘",
            "status": True
        }
    else:
        data = DataModel(appname=dataModel.appname, datajson=dataModel.datajson, clientName=dataModel.clientName)
       
        data = data.save()
        return {
            "message":"Thank tou bro 😘",
            "status": True
        }
        
        
@app.get("/get-data-xxxxxxx-data")
async def getData():
    findData = DataModel.objects.all()
    data = findData.to_json()
    fromjson = json.loads(data)
    return fromjson

@app.get("/api/v1/search-data/{searchname}/{appname}")
async def searchData(searchname: str, appname: str):
    findquery = DataModel.objects(clientName=searchname, appname=appname).first()
    tojson = findquery.to_json()
    fromjson = json.loads(tojson)
    return fromjson