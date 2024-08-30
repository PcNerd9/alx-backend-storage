#!/usr/bin/env python3

"""
contains a function that provides stats about Nginx
logs stored in Mongodb
"""

from pymongo import MongoClient

def main():
    """ The main entrance to the program
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx

    total_count = collection.count_documents({})
    get_count = collection.count_documents({"method": "GET"})
    post_count = collection.count_documents({"method": "POST"})
    put_count = collection.count_documents({"method": "PUT"})
    patch_count = collection.count_documents({"method": "PATCH"})
    delete_count = collection.count_documents({"method": "DELETE"})
    status = collection.count_documents({"path": "/status"})

    print("{} logs".format(total_count))
    print("Methods:")
    print("\tmethod GET: {}".format(get_count))
    print("\tmethod POST: {}".format(post_count))
    print("\tmethod PUT: {}".format(put_count))
    print("\tmethod PATCH: {}".format(patch_count))
    print("\tmethod DELETE: {}".format(delete_count))
    print("{} status check".format(status))

if __name__ == "__main__":
    main()
