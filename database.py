from pymongo import MongoClient


def getDatabase():
    # Replace the uri string with your MongoDB deployment's connection string.
    uri = "mongodb+srv://cz4052:jq2Iq8rebMS6u9Qj@cluster0.eud33pz.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    return client['love_checker_database']

    # client.close()


def getCollection(dbName):
    return dbName["love_checker"]


def getDocuments(collectionName):
    document1 = {
        "message": "I love you",
        "love": 0,
        "neutral": 0,
        "hate": 0
    }

    document2 = {
        "message": "Please leave me alone, I do not like you",
        "love": 0,
        "neutral": 0,
        "hate": 0
    }

    collectionName.insert_many([document1, document2])


if __name__ == "__main__":
    dbName = getDatabase()
    collectionName = getCollection(dbName)
    getDocuments(collectionName)
