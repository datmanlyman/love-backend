from pymongo import MongoClient
import pandas as pd


def getDatabase():
    # Replace the uri string with your MongoDB deployment's connection string.
    uri = "mongodb+srv://cz4052:jq2Iq8rebMS6u9Qj@cluster0.eud33pz.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    return client['love_checker_database']

    # client.close()


def getCollection(dbName):
    return dbName["love_checker"]


'''
def getDocuments(collectionName):
    document1 = {
        "message": "<3",
        "love": 0,
        "neutral": 0,
        "hate": 0
    }

    document2 = {
        "message": "</3",
        "love": 0,
        "neutral": 0,
        "hate": 0
    }

    collectionName.insert_many([document1, document2])
'''


if __name__ == "__main__":
    dbName = getDatabase()
    collectionName = getCollection(dbName)
    love_df = pd.DataFrame(columns=["message", "sentiment"])

    for record in collectionName.find():
        winner = ""

        if record["love"] == record["hate"] == record["neutral"]:
            winner = "neutral"
        elif record["love"] > record["hate"] and record["love"] > record["neutral"]:  # love is most
            winner = "love"
        elif record["hate"] > record["love"] and record["hate"] > record["neutral"]:  # hate is most
            winner = "hate"
        elif record["neutral"] > record["love"] and record["neutral"] > record["hate"]:  # neutral is most
            winner = "neutral"
        elif record["love"] == record["neutral"]:
            winner = "love"
        elif record["hate"] == record["neutral"]:
            winner = "hate"
        elif record["love"] == record["hate"]:
            winner = "neutral"

        love_df = love_df.append(
            {"message": record["message"], "sentiment": winner}, ignore_index=True)

    print(love_df)
