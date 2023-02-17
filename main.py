from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/checkLove", methods=["POST"])
def checkLove():
    # get parameters from request body
    text = request.json["text"]

    print(text)

    # do your NPL stuff here

    # return response
    return jsonify({"result": text})


@app.route("/crowdResponse", methods=["POST"])
def crowdResponse():
    # get parameters from request body
    text = request.json["text"]

    print(text)

    # do your NPL stuff here

    # return response
    return jsonify({"result": text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
