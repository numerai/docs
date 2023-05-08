# Submissions

## Round Lifecycle

Each round goes through 4 stages over the span of a month:

* Open: when new live features are released
* Close: when live predictions must be submitted
* Score: when live submission scores are computed
* Resolve: when the final score and payouts are resolved

The tournament is organized into rounds starting Saturday, Tuesday, Wednesday, Thursday and Friday every week.&#x20;

With each round spanning one month and 5 new rounds starting each week, we end up with an overlapping round schedule. At any given time, we can have up to 25 overlapping resolving rounds.  &#x20;

Here is a visualization of the schedule of tournament rounds.

<figure><img src="../../.gitbook/assets/image (95).png" alt=""><figcaption></figcaption></figure>

## Round Schedule

We generally we expect rounds to follow this schedule:

| Round   | Open          | Close         |
| ------- | ------------- | ------------- |
| Sat-Mon | Sat 18:00 UTC | Mon 14:30 UTC |
| Tue     | Tue 13:00 UTC | Tue 14:00 UTC |
| Wed     | Wed 13:00 UTC | Tue 14:00 UTC |
| Thu     | Thu 13:00 UTC | Thu 14:00 UTC |
| Fri     | Fri 13:00 UTC | Fri 14:00 UTC |

Actual open and close times may vary from round to round, but we will always maintain a minimum 1 hour submission window.

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
live_features = live_data[[f for f in live_data.columns if "feature" in f]]

# Generate live predictions
live_predictions = model.predict(live_features)

# Format submission
submission = pd.Series(live_predictions, index=live_features.index).to_frame("prediction")
submission.to_csv(f"prediction_{current_round}.csv")

# Upload submission 
napi.upload_predictions(f"prediction_{current_round}.csv", model_id="your-model-id")
```

## Automation

There are many ways to automate your submission pipeline and which way you choose depends on your needs.

If you want to go with a production-grade cloud hosted solution, Numerai has built two frameworks to help you setup and deploy your submission pipeline to AWS:

* [Compute Heavy](broken-reference): If you have a big and complex submission pipeline&#x20;
* [Compute Lite (Beta)](https://docs.google.com/document/d/1RCKgL4SAqEJ2atnMsdaPHdlV-d7pxJl9dB\_\_mSx11CM/edit?usp=sharing): If you have a small and simple submission pipeline

If you like the cloud but prefer a more barebones / DIY setup, check out these examples on Google Cloud

* [Google Cloud VM Example](https://forum.numer.ai/t/automated-submission-with-google-cloud/3888)
* [Google Cloud Function Example](https://github.com/Raynos/numerai-example)

If you want use your own server, check out these examples

* [CRON example](https://forum.numer.ai/t/automated-submissions-from-bash-shell-script/5806)
* [NGROK example](https://github.com/Raynos/numerai-example/tree/ngrok-test) &#x20;
