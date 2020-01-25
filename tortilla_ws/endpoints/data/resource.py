from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from app import db
import json

user_post_parser = reqparse.RequestParser()


class DataResource(Resource):
    def get(self, user_id=None):
        _data = {'Task': 'Hours per Day', 'Work': 11, 'Eat': 2, 'Commute': 2, 'Watch TV': 2, 'Sleep': 7 }


        cols[0]=""
        cols[1]=""
        
        rows[0]=""
        rows[1]=""
        
        
        struct[0]= cols
        struct[1]= rows

        return struct
