from flask import Flask, request, jsonify
import joblib
import pandas
from sklearn.preprocessing import LabelEncoder
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
@cross_origin(supports_credentials=True)
def predict():
    try:
        # get data
        raw = pandas.read_csv("../data/heart_2022_no_nans.csv")
        unimportant_features = ["RemovedTeeth", "DeafOrHardOfHearing", "BlindOrVisionDifficulty", "DifficultyDressingBathing", \
                        "DifficultyErrands", "DifficultyWalking"]
        raw = raw.drop(unimportant_features, axis=1)
        encoder = LabelEncoder()
        X = raw.drop("HadHeartAttack", axis=1)

        # make sure to put a dictionary/object mapping X column to raw value in record
        input_data = request.json['record']
        if "HadHeartAttack" in input_data:
            del input_data["HadHeartAttack"]
        for feature in unimportant_features:
            if feature in input_data:
                del input_data[feature]

        # encode record by fitting to X data
        for i in X.columns:
            encoder = LabelEncoder()
            encoder.fit(X[i])
            input_data[i] = encoder.transform([input_data[i]])[0]
        
        print(input_data)
        
        # create final test record
        y_test = []
        for i in X.columns:
            y_test.append(input_data[i])
        
        print(y_test)
        # make predictions using data
        model = joblib.load('random_forest.joblib')
        prediction = model.predict([y_test])[0]
        # return the prediction as a JSON response and cast int64 to int
        return jsonify({'prediction': int(prediction)}), 200
    except Exception as e:
        # handle any errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)