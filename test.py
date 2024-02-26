from bson.objectid import ObjectId
from hw_project.quotes.utils import get_mongodb
# import mongoengine

db = get_mongodb()
# authors = []
# base = db.authors.find()

# for author in base:
#     authors.append(author)

# print(authors)

# author = db.authors.find_one({'_id': ObjectId('65c202d30a7d4fb7686726e6')})

a = db.authors.objects

print(a)