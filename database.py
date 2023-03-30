from pymongo import MongoClient
import pandas as pd
import csv


def getDatabase():
    # Replace the uri string with your MongoDB deployment's connection string.
    uri = "mongodb+srv://cz4052:jq2Iq8rebMS6u9Qj@cluster0.eud33pz.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    return client['love_checker_database']

    # client.close()


def getCollection(dbName):
    return dbName["love_checker"]


def getDocuments(collectionName):
    document_1 = {
        "message": "What do you think of the person I am crushing on?",
        "love": 0,
        "neutral": 0,
        "hate": 1
    }

    collectionName.insert_one(document_1)


def csvToDB(file, collectionName):
    with open(file, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            collectionName.insert_one(rows)
    print("Success!")


if __name__ == "__main__":
    dbName = getDatabase()
    collectionName = getCollection(dbName)
    getDocuments(collectionName)
    # csvToDB('dummy_love_data - Sheet2.csv', collectionName)
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
