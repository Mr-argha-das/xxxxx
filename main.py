from mongoengine import connect, Document, StringField, DateTimeField
from fastapi import FastAPI, HTTPException

import datetime
import json
app = FastAPI()

connect('securedata', host="mongodb+srv://sahiljoya11:sahil1122@cluster0.syubkoh.mongodb.net/securedata")

class DataModel(Document):
    appname= StringField(required=True, max_length=200)
    datajson = StringField(required=True, max_length=255)
    clientName = StringField(required=True, max_length=200)
    created = StringField(default=f"{datetime.date.today()}")
    
    
@app.post("/api/v1/create-data")
async def createData(appname:str, datajson: str, clientName: str):
    findData = DataModel.objects(clientName=clientName).first()
    if findData:
        findData.delete()
        data = DataModel(appname=appname, datajson=datajson, clientName=clientName)
        data = data.save()
        return {
            "message":"Thank tou bro 😘",
            "status": True
        }
    else:
        data = DataModel(appname=appname, datajson=datajson, clientName=clientName)
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