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

<figure><img src="../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

## Submission Window

We generally expect rounds to follow this schedule:

| Round   | Open          | Close         |
| ------- | ------------- | ------------- |
| Sat-Mon | Sat 18:00 UTC | Mon 14:30 UTC |
| Tue     | Tue 13:00 UTC | Tue 14:00 UTC |
| Wed     | Wed 13:00 UTC | Wed 14:00 UTC |
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

#### Model Uploads

The simplest way to automate your submissions is to upload your entire prediction pipeline to Numerai. Once uploaded, Numerai will take care of running it every day to generate live submissions.

See [model upload](model-uploads.md) section for more details.

#### Official Cloud Solutions

If you prefer to run your own automation or have a more complex model or pipeline, we recommend an official cloud solution since we actively support these and any bug reports / support issues can be addressed by us directly. We have also engineered these to be highly reliable and very low cost.

* [Compute Lite](https://docs.google.com/document/d/1RCKgL4SAqEJ2atnMsdaPHdlV-d7pxJl9dB\_\_mSx11CM/edit?usp=sharing) - use AWS and Sagemaker to deploy a medium complexity model
* [Compute Heavy](https://github.com/numerai/numerai-cli) - use AWS or Azure to deploy a more complex pipeline

#### DIY for Google Cloud

If you're more comfortable with GCP, our users have provided some DIY solutions. These are not officially supported so you should already be comfortable with GCP if you choose one of these.

* [Google Cloud Function Example](https://github.com/Raynos/numerai-example) - lower resources available, lower cost, simple
* [Google Cloud VM Example](https://forum.numer.ai/t/automated-submission-with-google-cloud/3888) - more resources available, variable cost, less simple

#### DIY for your local computer

If you prefer to keep things on-premises you can go with one of these. They are relatively simple and cheap, but running your own local computer comes with the burden of ensuring reliability and running your own tech support.

* [CRON example](https://forum.numer.ai/t/automated-submissions-from-bash-shell-script/5806) - scheduling your script to run regularly and detect when to submit
* [NGROK example](https://github.com/Raynos/numerai-example/tree/ngrok-test)  - setup a webhook for Numerai to notify you when to submit

## Multiple Submissions

You can upload as many submissions as you would like during a round's submission window, but only the latest valid submission will be "selected" for scoring and payouts.&#x20;

## Late Submissions

If you miss the submission window of the current round, you are still allowed to upload your submission but it will be considered "late".

A late submission is still scored on CORR (and other secondary scores) but will not receive a TC score. This is because TC is a measure of your submission's contribution to the hedge fund returns and the meta model is constructed and trading happens immediately after the submission deadline. If your submission is late, it means that  it was not included in the meta model and therefore has precisely 0 impact on the hedge fund returns.&#x20;

A late submission is also not eligible for staking and payouts for the round. The "at-risk" NMR number of a late submission is automatically set to 0 and excluded in the payout factor calculation.

## Queued and Delayed Submissions

If you miss the submission window of the current round, your submission will be automatically "queued" for the upcoming round.&#x20;

Queued submissions turn into on-time submissions immediately after the upcoming round opens. Since the ids of the live data changes every round, Numerai will automatically map your prediction's ids from the previous round to the latest round's ids.

If your pipeline takes too long to run (ie over 24 hours), you may use your predictions generated for the previous round to submit in the current round. Again, since the ids of the live data changes every round, Numerai will automatically map your delayed prediction's ids from the previous round to the latest round's ids.
