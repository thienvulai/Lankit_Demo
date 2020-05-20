from src.app import db


class RequestMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    message = db.Column(db.String(100), nullable=False)


# import uuid
# from typing import Dict
# from src.common import Database
#
#
# class RequestMessage:
#     def __init__(self, fullname: str, email: str, message: str, _id: str = None):
#         self.fullname = fullname
#         self.email = email
#         self.message = message
#         self.table = 'RequestMessages'
#         self._id = _id or uuid.uuid4().hex
#
#     def json(self) -> Dict:
#         return {
#             "_id": self._id,
#             "fullname": self.fullname,
#             "email": self.email,
#             "message": self.message
#         }
#
#     def save_to_db(self):
#         Database.insert(self.table, self.json())
