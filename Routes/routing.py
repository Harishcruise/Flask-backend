from flask_pymongo import pymongo
from flask import jsonify, request
# import pandas as pd

con_string = "mongodb+srv://HarishCruise:Jamestay007@harishserver.ve6hz2a.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_string)

db = client.get_database('Demo')

user_collection = pymongo.collection.Collection(db, 'Test')
print("MongoDB connected Successfully")

def route_endpoint(endpoints):
    @endpoints.route('/PostData', methods=['POST'])
    def PostData():
        resp = {}
        try:
            req_body = request.json
            user_collection.insert_one(req_body)            
            print("User Data Stored Successfully in the Database.")
            status = {
                "statusCode":"200",
                "statusMessage":"Successful."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        resp["status"] =status
        return resp

    @endpoints.route('/GetData', methods=['GET'])
    def GetData():
        resp = {}
        try:
            users = user_collection.find({})
            print(users)
            users = list(users)
            status = {
                "statusCode":"200",
                "statusMessage":"Successful."
            }
            output = [{'ID' : user['id'],'Name' : user['name'], 'Email' : user['gmail']} for user in users]   #list comprehension
            resp['data'] = output
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        resp["status"] =status
        return resp

    @endpoints.route('/PutData',methods=['PUT'])
    def PutData():
        resp = {}
        try:
            req_body = request.json
            # req_body = req_body.to_dict()
            user_collection.update_one({"id":req_body['id']}, {"$set": req_body['body']})
            print("Successful.")
            status = {
                "statusCode":"200",
                "statusMessage":"Successful."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        resp["status"] =status
        return resp    

    @endpoints.route('/DeleteData',methods=['DELETE'])
    def DeleteData():
        resp = {}
        try:
            delete_id = request.args.get('delete_id')
            user_collection.delete_one({"id":delete_id})
            status = {
                "statusCode":"200",
                "statusMessage":"Successful."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        resp["status"] =status
        return resp
    
    
    return endpoints