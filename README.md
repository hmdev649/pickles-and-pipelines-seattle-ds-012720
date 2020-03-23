# Introduction to Pickles and Pipelines

## `pipeline-env`

To reproduce the `pipeline-env` conda environment, please run the following bash commands:

```bash
# create pipeline-env from the environment.yml file
conda env create -f environment.yml

# add pipeline-env as a kernel in jupyter
python -m ipykernel install --user --name=pipeline-env
```

## Google Cloud Functions
Google Cloud Functions allow you to make a single function that can be called from a REST API interface.  The Python language versions are actually running on top of Flask, with as much boilerplate removed as possible.  So you still need to learn some Flask to be able to get everything working.

### Pricing
Up to 2 million free Cloud Function invocations per month.  [Free tier](https://cloud.google.com/free/) requires signing up with a credit card, but promises "No autocharge after free trial ends"

### Pros
 - Free
 - Makes a REST API interface, so you can demo with Postman or an HTML + JS web frontend (or collaborate with an SE alum to make a React frontend for you)
 - Only requires you to learn a little bit of Flask.  Nothing about production WSGI servers, or nginx, or ports.

### Cons
 - Not making a full-stack web app means you won't have the experience of making a full-stack web app
 - Sometimes there is a lot of "magic" happening with the implicit Flask app that makes it hard to debug.  Probably will not be compatible with TensorFlow, for example, because you don't have fine-grained control over the threading behavior.
 - If you want to deploy a web frontend, you'll need to find another tool.  (GitHub Pages works fine though!)
 - The platform is not designed specifically for ML models, so it might be annoyingly slow, or even so slow that it times out.
 - You can't generate any data visualizations in Python, they will have to be in JavaScript

### Documentation
1. [Writing cloud functions](https://cloud.google.com/functions/docs/writing/http)
2. [Deploying cloud functions](https://cloud.google.com/functions/docs/deploying/filesystem)
3. [Calling cloud functions](https://cloud.google.com/functions/docs/calling/http)

### Example
I have a working example of a Google Cloud function in the `google_cloud_function` folder.  You can call it right now by pasting this into your terminal:
```
curl -X POST -H "Content-type: application/json" -d '{"Alcohol": 12.82, "Malic acid": 3.37, "Ash": 2.3, "Alcalinity of ash": 19.5, "Magnesium": 88.0, "Total phenols": 1.48, "Flavanoids": 0.66, "Nonflavanoid phenols": 0.4, "Proanthocyanins": 0.97, "Color intensity": 10.26, "Hue": 0.72, "OD280/OD315 of diluted wines": 1.75, "Proline": 685.0}' https://us-central1-splendid-petal-256700.cloudfunctions.net/wine-predictor
```