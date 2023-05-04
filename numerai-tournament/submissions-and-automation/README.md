# Submissions & Automation

## Submissions

To compete in the tournament you must submit live predictions in every round.

Here is an example of how to make a submission in Python using [NumerAPI](https://github.com/uuazed/numerapi):

```python
# Authenticate
napi = numerapi.NumerAPI("api-public-id", "api-secret-key")

# Get current round
current_round = napi.get_current_round()

# Download latest live features
napi.download_dataset(f"v4.1/live_{current_round}.parquet")
live_data = pd.read_parquet(f"v4.1/live_{current_round}.parquet")
live_features = live_data[f for f in live_data.columns if "feature" in f]

# Generate live predictions
live_predictions = model.predict(live_features)
live_predictions.to_csv(f"prediction_{current_round}.csv")

# Submit predictions 
napi.upload_predictions(f"prediction_{current_round}.csv", model_id="your-model-id")
```

## Automation

There are many ways to automate your submission pipeline and which way you choose depends on your needs.

If you want to go with a production-grade cloud hosted solution, Numerai has built two frameworks to help you setup and deploy your submission pipeline to AWS.&#x20;

* [Compute Heavy](broken-reference): If you have a big and complex submission pipeline&#x20;
* [Compute Lite (Beta)](https://docs.google.com/document/d/1RCKgL4SAqEJ2atnMsdaPHdlV-d7pxJl9dB\_\_mSx11CM/edit?usp=sharing): If you have a small and simple submission pipeline

If you like the cloud but prefer a more barebones setup, check out these examples on Google Cloud&#x20;

* [Google Cloud VM Example](https://forum.numer.ai/t/automated-submission-with-google-cloud/3888)
* [Google Cloud Function Example](https://github.com/Raynos/numerai-example)

If you want use your own server, check out these examples

* [CRON example](https://forum.numer.ai/t/automated-submissions-from-bash-shell-script/5806)
* [NGROK example](https://github.com/Raynos/numerai-example/tree/ngrok-test) &#x20;
