---
description: Submitting your predictions to Numerai
---

# Submissions

## Rounds

Each submission is associated with a "Round" of the tournament.

Each round goes through 4 stages over the span of a month:

* Open: the start of a new round and new live features are released
* Close: the cutoff for when live predictions must be submitted
* Score: the days that submissions are given scores
* Resolve: when final scores and payouts are resolved

A new round starts each day Tuesday through Saturday. Each round spans about one month, so with 5 new rounds starting each week, we end up with an overlapping round schedule. At any given time, we can have up to 25 overlapping rounds.  &#x20;

Here is a visualization of the schedule of tournament rounds:

<figure><img src="../../.gitbook/assets/image (39).png" alt=""><figcaption><p>Visual representation of Rounds 453 - 477 overlapping</p></figcaption></figure>

Notice that rounds starting Saturday occupy the full weekend - opening on Saturday and closing on Monday - whereas Rounds starting Tuesday through Friday are open only for 1 hour. Also notice that there are no scores released on Sundays and Mondays.

We generally expect rounds to follow this schedule:

<table><thead><tr><th width="99">Round</th><th width="148">Open Time*</th><th width="148">Close Time*</th><th width="125">Scores Start</th><th>Resolve Time</th></tr></thead><tbody><tr><td>Tue</td><td>Tue 13:00 UTC</td><td>Tue 14:00 UTC</td><td>Next Sat.</td><td>~31 days later (Fri.)</td></tr><tr><td>Wed</td><td>Wed 13:00 UTC</td><td>Wed 14:00 UTC</td><td>Next Tue.</td><td>~31 days later (Sat.)</td></tr><tr><td>Thu</td><td>Thu 13:00 UTC</td><td>Thu 14:00 UTC</td><td>Next Wed.</td><td>~33 days later (Tue.)</td></tr><tr><td>Fri</td><td>Fri 13:00 UTC</td><td>Fri 14:00 UTC</td><td>Next Thu.</td><td>~33 days later (Wed.)</td></tr><tr><td>Sat</td><td>Sat 13:00 UTC</td><td>Mon 14:30 UTC</td><td>Next Fri.</td><td>~33 days later (Thu.)</td></tr></tbody></table>

\*Actual open and close times may vary from round to round, but we will always maintain a minimum 1 hour submission window and guarantee that Rounds will **open** **no earlier than 13:00 UTC and end no earlier than 14:00 UTC.**

## Making a Submission

To properly compete in the tournament you should submit live predictions in every round.

Here is an example of how to make a submission in Python using [NumerAPI](https://github.com/uuazed/numerapi):

```python
from numerapi import NumerAPI
import pandas as pd

# Authenticate
napi = NumerAPI("[your api public id]", "[your api secret key]")

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

### Multiple Submissions

You can upload as many submissions as you would like during this submission window, but only the latest valid submission will be "selected" for scoring and payouts.

### Late Submissions

If you miss the submission window of the current round, you are still allowed to upload your submission but it will be considered "late" - it still gets scored, but you cannot stake on it. Late submissions do not impact the Meta Model, the "at-risk" NMR of a late submission is 0, and its does not impact the payout factor for other users (see.

## Automation

### Model Uploads

The simplest (and most restrictive) way to automate your submissions is to upload your trained model to Numerai. Once uploaded, Numerai will handle generating and submitting predictions for you every day. Use this if you don't like dealing with infrastructure.

See [model upload](model-uploads.md) section for more details.

### Numerai-CLI

Also known as "Compute Heavy", this is an official self-hosted cloud solution that supports AWS, GCP, or Azure. If you prefer to run your own automation or have a more complex model or pipeline, we recommend using Numerai CLI. We actively support this framework and directly respond to any bug reports / support issues. We have also engineered it to be highly reliable and very low cost.

Read more about this on the [Numerai-CLI Github page](https://github.com/numerai/numerai-cli).

### Local Server

If you prefer to keep things on-premises you can go with one of these. They are relatively simple and cheap, but running your own local computer comes with the burden of ensuring reliability and running your own tech support.

* [CRON example](https://forum.numer.ai/t/automated-submissions-from-bash-shell-script/5806) - scheduling your script to run regularly and detect when to submit
* [NGROK example](https://github.com/Raynos/numerai-example/tree/ngrok-test)  - setup a webhook for Numerai to notify you when to submit

## Queued and Delayed Submissions

If you miss the submission window of the current round, your submission will be automatically "queued" for the upcoming round.&#x20;

Queued submissions turn into on-time submissions immediately after the upcoming round opens. Since the ids of the live data changes every round, Numerai will automatically map your prediction's ids from the previous round to the latest round's ids.

If your pipeline takes too long to run (ie over 24 hours), you may use your predictions generated for the previous round to submit in the current round. Again, since the ids of the live data changes every round, Numerai will automatically map your delayed prediction's ids from the previous round to the latest round's ids.
