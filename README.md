# heart-disease-dva

## Running the frontend

On the root directory, run the Python server:

```
python -m http.server
```

This will run a local server on port 8000 where you can access the application. Go on `localhost:8000` and access the pages you wish to view. The pages include our Bayesian estimator, results from our model, as well as correlation between attributes.

## View the trained and fine-tuned model

If you want to check out the notebook where the data was preprocessed and the model was trained, you may view `model/CSE_6242_Final.ipynb`.

## Running the backend Flask server

Install the following packages and versions using `conda` (if you already have them, please remove them before using `conda remove <package>`):

```
conda install scikit-learn=1.2.
conda install conda-forge::joblib
conda install pandas=2.0.3
conda install flask
```

On the `model/` directory, run the Python Flask server:

```
flask run --no-debugger
```

This will run a local Flask server on port 5000. Make sure to have it running for model results.

## Dataset

https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease?resource=download
