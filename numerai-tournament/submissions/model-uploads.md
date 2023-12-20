---
description: Free, zero-setup automation
---

# Model Uploads

## Introduction

Model uploads is a simple and free way to automate your daily submissions.

## How it works&#x20;

1. Wrap your model in a function that takes live features and outputs live predictions
2. Pickle your function with the [cloudpickle](https://github.com/cloudpipe/cloudpickle) library and upload the pickle file to Numerai
3. Numerai will run your model every day to generate live predictions in the [numerai-predict](https://github.com/numerai/numerai-predict) execution environment

<figure><img src="https://lh3.googleusercontent.com/XthD6GjwyuPt036TdPBVnj1yxUPGs5bmV5nv1AXSo-QhJnIwkKauoFwvvqKrWOTJ-JgN8zktL0tz3ctpzyuEnTBg3TdbnH3R6k478X4jq5bgoIz4zJwgrTJHcIk8eSDw4Dp7AfWQkN3rDUo_MONKo8E" alt=""><figcaption></figcaption></figure>

## How to pickle your model

Once you have a trained model that you are ready to upload, simply wrap it with a function that takes live features and outputs live predictions.

```python
# Wrap your model with a function that takes live features and returns live predictions
def predict(live_features: pd.DataFrame) -> pd.DataFrame:
    live_predictions = model.predict(live_features[feature_cols])
    submission = pd.Series(live_predictions, index=live_features.index)
    return submission.to_frame("prediction")
```

Then, use the [cloudpickle](https://github.com/cloudpipe/cloudpickle) library to serialize your function into a file.&#x20;

```python
# Use the cloudpickle library to serialize your function
import cloudpickle
p = cloudpickle.dumps(predict)
with open("predict.pkl", "wb") as f:
f.write(p)
```

See [this notebook](https://colab.research.google.com/github/numerai/example-scripts/blob/master/hello\_numerai.ipynb) for a full tutorial or [this notebook](https://colab.research.google.com/github/numerai/example-scripts/blob/master/example\_model.ipynb) for a barebones example.&#x20;

## How to upload your pickle file

Head to [numer.ai/submissions](http://numer.ai/submissions) and find the Upload Model button on the right side of the models table.&#x20;

![](<../../.gitbook/assets/image (106).png>)

Click on the Upload Model button to open the modal upload modal. Select the pickle file you wish to upload, set the Python version used to create the pickle, then click Upload.&#x20;

![](<../../.gitbook/assets/image (123).png>)

Once your upload is complete, Numerai will immediately run your model to generate a live submission for the current round and against the validation dataset to generate diagnostics.&#x20;

<figure><img src="https://documents.lucid.app/documents/1ac83fbf-7df7-4f26-a606-f04b8c742692/pages/0_0?a=278&#x26;x=-1896&#x26;y=-1052&#x26;w=1892&#x26;h=255&#x26;store=1&#x26;accept=image%2F*&#x26;auth=LCA%2036ee9770a1f7aecad5f59dead64e8b85373184e69f69a7f345e0e14ef1596de7-ts%3D1687892551" alt=""><figcaption></figcaption></figure>

Once these complete, you should see a submission block in the submissions column, the success status under the latest submission column, a link to view diagnostics under diagnostics column.

<figure><img src="https://documents.lucid.app/documents/1ac83fbf-7df7-4f26-a606-f04b8c742692/pages/0_0?a=317&#x26;x=-1827&#x26;y=-831&#x26;w=1690&#x26;h=242&#x26;store=1&#x26;accept=image%2F*&#x26;auth=LCA%2017f77d78498ba7e3f5486e98afb16cf1b0fa69909ea695f4bf00a4a009cfb7ab-ts%3D1687892551" alt=""><figcaption></figcaption></figure>

## How to track your submission status

If everything is working correctly, you will see the latest submission cycle through these 4 statuses:

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

## Understanding Cloudpickle

[Cloudpickle](https://github.com/cloudpipe/cloudpickle) is a library that allows you to easily run your local Python code remotely in the cloud. It is used behind the scenes by many popular distributed computing frameworks like [Dask](https://www.dask.org/) and [Ray](https://www.anyscale.com/ray-open-source).

The main benefit of using cloudpickle over the [pickle](https://docs.python.org/3/library/pickle.html) standard library is that it serializes your local context along with your code. This makes it very convenient to package up code developed locally in a notebook environment like Google Colab.

In the example below, our function references `model` and `feature_cols`  defined in the global scope. Cloudpickle is smart enough to correctly serialize both  `model` and `feature_cols` by value so that it is also available when this function is run by Numerai.

```python
def predict(features: pd.DataFrame) -> pd.DataFrame:
   # model and feature_cols are defined in the global scope
   live_predictions = model.predict(features[feature_cols])
   submission = pd.Series(live_predictions, index=features.index)
   return submission.to_frame("prediction")
```

## Understanding Numerai Predict

[Numerai-predict](https://github.com/numerai/numerai-predict) is the execution environment for your model.

Since cloudpickle does not serialize Python itself or Python libraries in your local environment, you will need to make sure that your code is compatible with the exact Python versions listed and libraries supported in the [requirements.txt](https://github.com/numerai/numerai-predict/blob/master/requirements.txt).&#x20;

When debugging issues, it may be helpful to download the numerai-predict docker container for local testing.

We aim to support all industry standard python machine learning libraries. If your pipeline is using a library that is not currently unsupported, please let us know and we will consider adding it.&#x20;

## Resource constraints and limitations

For security reasons, your uploaded model will have no access to the internet.&#x20;

By default, we will provision each model a machine with 1 CPU with 4GB of ram and allow runtime of up to 10 minutes (does not include time spent queueing).

Benchmarks:

* LGBM model with 20K trees (in example notebooks above) using the small feature set runs in under 1 minute&#x20;
* LGBM model with 90K trees using the full feature set runs in under 6 minutes&#x20;

## Interactions with submission upload and compute

To avoid race conditions, you will need to disable any existing compute configuration in order to upload your model.&#x20;

Similarly, once you upload your model, you will no longer be able to upload submissions via the API or configure compute on your model.

## Why you may not want to use this feature

This feature is designed for new and intermediate users who don’t want to invest time in setting up and managing their own model hosting infrastructure.

The obvious downside of this feature is that you need to upload (and give Numerai access to) your trained model. If you are not comfortable with this, you are 100% free to continue using Compute Heavy, Compute Lite or any [other automation solution](https://docs.numer.ai/numerai-tournament/submissions#automation) of your choice.

## Terms of service

Numerai reserves the right to disable your model for any reason, including security concerns or if your account is no longer active.

Numerai will try our best to support your usage of this feature but ultimately it is still your responsibility to make sure your submission pipeline is set up properly.
