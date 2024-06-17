---
description: Free, zero-setup automation
---

# Model Uploads

## Introduction

Model uploads are a simple and free way to automate your daily submissions. You upload a `.pkl`file with your trained model and we handle generating and submitting the predictions for you. You don't need to worry about reliability, infrastructure, scheduling, etc. **you just focus on data science.**

See [this notebook](https://colab.research.google.com/github/numerai/example-scripts/blob/master/hello\_numerai.ipynb) for a full tutorial or [this notebook](https://colab.research.google.com/github/numerai/example-scripts/blob/master/example\_model.ipynb) for a barebones example.&#x20;

## How it works

### 1. Trained Model

Install requirements from the [Numerai Predict](https://github.com/numerai/numerai-predict/blob/master/requirements.txt) execution environment and train a model. These are strict package version requirements that will help ensure your model always runs correctly. You may try to install later minor versions / patches of the packages listed as long as it is backwards-compatible with this environment.&#x20;

Anything not listed is not available, but we do take requests over on [Discord](https://discord.gg/numerai).

### 2. Prediction Pipeline

Wrap your model in a function that takes live features and outputs live predictions:

```python
# Wrap your model with a function that takes live features and returns live predictions
def predict(live_features: pd.DataFrame) -> pd.DataFrame:
    live_predictions = model.predict(live_features[feature_cols])
    submission = pd.Series(live_predictions, index=live_features.index)
    return submission.to_frame("prediction")
```

This is the only way for Numerai to properly run your model for you. If your pickle doesn't have a predict function with this signature, it will fail.

### 3. Cloudpickle

Pickle your function with the [cloudpickle](https://github.com/cloudpipe/cloudpickle) library and upload the pickle file to Numerai:

```python
# Use the cloudpickle library to serialize your function
import cloudpickle
p = cloudpickle.dumps(predict)
with open("predict.pkl", "wb") as f:
f.write(p)
```

This library  is used in other computing frameworks like [Dask](https://www.dask.org/) and [Ray](https://www.anyscale.com/ray-open-source) and allows you to easily run your local Python code remotely in the cloud. The main benefit of using cloudpickle over the standard [pickle](https://docs.python.org/3/library/pickle.html) library is that it serializes your local context along with your code. This makes it very convenient to package up code developed locally in any environment.

In the example above, our `predict` function references `model` and `feature_cols`  defined in the global scope. Cloudpickle is smart enough to correctly serialize both  `model` and `feature_cols` by value so that it is also available when this function is run by Numerai.

### 4. Upload the Pickle

Upload your Model on the [Submissions page](http://numer.ai/submissions) (the Upload Model button on the right):

<div align="center">

<figure><img src="../../.gitbook/assets/image (106).png" alt="" width="224"><figcaption></figcaption></figure>

</div>

Select your pickle file, set the Python version you used, then click Upload

<figure><img src="../../.gitbook/assets/image (123).png" alt="" width="295"><figcaption></figcaption></figure>

Numerai will execute your model to generate a live submission for the current round:

<figure><img src="../../.gitbook/assets/Screenshot 2024-03-18 at 3.29.52 PM.png" alt=""><figcaption></figcaption></figure>

If this succeeds, a block will appear in the "submissions" column grid, you'll be able to review the execution logs for your model, and Numerai will generate diagnostics over the validation dataset for your model:

<figure><img src="../../.gitbook/assets/Screenshot 2024-03-18 at 3.13.58 PM (1).png" alt=""><figcaption></figcaption></figure>

Once diagnostics complete, you'll also be able to view the diagnostics for this model:

<figure><img src="../../.gitbook/assets/Screenshot 2024-03-18 at 3.13.43 PM.png" alt=""><figcaption></figcaption></figure>

### 5. Running Daily

Once uploaded, Numerai runs your model every day to generate and submit live predictions for you. If everything is working correctly, you will see the latest submission cycle through these 4 statuses:

1. Pending: Numerai is provisioning the cloud resources to run your model
2. Running: Numerai is now running your model&#x20;
3. Validating: Numerai has ran your model and is now validating your submission
4. Success: Numerai has accepted your submission

If there was a problem, you will see 2 possible statuses:

1. Error: Numerai has encountered an unexpected error running your model and the team will look into it.
2. Failed: Your model failed to run. Please check the logs and re-upload a working model. Examples of model failures include
   * Python or dependency version mismatch
   * Invalid submission&#x20;
   * Out of memory
   * Timeout&#x20;

<figure><img src="https://lh5.googleusercontent.com/LgpMWSaDZ8W4M_pCIBX1qtDLWCZTfZiRklRs2HGN8K-_yJE3E40q9A_JvOZB8KbLWIn87DBIB2G8FV4rGGOCzWmfkvtRtjQVRTKS79i1kHfkjiWcq5zf8dBIW8t3fWypMVpJn4XIIfNVwSIOK0lzgqY" alt=""><figcaption></figcaption></figure>

## FAQ

### Can my model access the internet?

No, we do not give your model internet access.

### What are the Mem / CPU limitations?

By default, we will provision each model a machine with 1 CPU with 4GB of ram and allow runtime of up to 10 minutes (does not include time spent queueing).&#x20;

LightGBM Benchmarks:

* 20K trees using the small feature set runs in under 1 minute&#x20;
* 90K trees using the full feature set runs in under 6 minutes&#x20;

### Can I still upload predictions manually?

No, once you upload your model, you will no longer be able to upload submissions via the API.

### Can I have a webhook on my model?

No, to avoid race conditions after you upload your model, you cannot configure any webhooks on it.  You will need to disable any existing compute configuration in order to upload your model.&#x20;

### Does Numerai have full access to my trained model?

Yes, Numerai has access to and can unpickle your trained model.  If you are not comfortable with this, you should consider using [another automation solution](https://docs.numer.ai/numerai-tournament/submissions#automation).

## Terms of service

Numerai reserves the right to disable your model for any reason, including (but not limited to) security, abuse, account inactivity, poor performance, etc.

Numerai will try our best to support your usage of this feature, but ultimately it is still your responsibility to make sure your submission pipeline is set up properly. We do not guarantee that your model will submit 100% of the time.

Numerai is not responsible for the gains or losses you might experience due to the performance of your uploaded model. You are solely responsible for the performance of the model.
