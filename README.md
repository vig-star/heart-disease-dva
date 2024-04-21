## heart-disease-dva

We have three folders data, model, and pages. As the names suggest our `data` folder contains our dataset, the `model` folder contains our (`CSE_6242_Project.ipynb`) interactive python notebook that hosts our model and `rf_model.py` executes our model to predict the risk of heart attack by creating an API endpoint. Lastly, our `pages` folder contains our frontend including the visualizations using d3.

## Running the frontend

On the root directory, run the Python server:

```
python -m http.server
```

This will run a local server on port 8000 where you can access the application. Go on `localhost:8000` and access the pages you wish to view. The pages include our Bayesian estimator, results from our model, as well as correlation between attributes.

## View the trained and fine-tuned model

If you want to check out the notebook where the data was preprocessed and the model was trained, you may view `model/CSE_6242_Project.ipynb`.

## Running the backend Flask server

Install the following packages and versions using `conda` (if you already have them, please remove them before using `conda remove <package>`):

```
conda install scikit-learn=1.2.2
conda install conda-forge::joblib
conda install pandas=2.0.3
conda install flask
conda install flask_cors
```

On a separate window, navigate to the `model/` directory and run the Python Flask server:

```
flask run --no-debugger
```

This will run a local Flask server on port 5000. Make sure to have it running for model results.

## Demo Video

https://youtu.be/BNuujoPwTsg

## Dataset

https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease?resource=download
