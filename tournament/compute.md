# Numerai CLI and Compute

Numerai CLI 0.3.0 is here! This update introduces breaking changes, so if you're already using Numerai CLI 0.1 or 0.2, please make sure you follow the upgrade guide below.

## Introduction

Numerai CLI \(Command Line Interface\) is a command line tool that helps you automate your weekly submission workflow by creating your own Numerai Compute Cluster and deploying Prediction Nodes to your cluster. The goal is to provision resources in the cloud for your Numerai models so they can automatically submit each week so you don't have to worry about getting burned by late submissions.

![Prediction Nodes in the Numerai Network ](../.gitbook/assets/architecture_prediction_network.png)

Use the [numerai-cli](https://github.com/numerai/numerai-cli) to provision your own cloud infrastructure and deploy your pre-trained model as a Prediction Node that can be triggered by Numerai to download new tournament data, run your model, and upload predictions to Numerai.

## Getting Started

You need 4 things to use Numerai CLI: Docker, Python3, Numerai API Keys, and AWS API Keys. If you want some help getting these, you can follow the documentation on the Github Repository:

[https://github.com/numerai/numerai-cli](https://github.com/numerai/numerai-cli)

If you have everything, you can get started right away:

```text
pip3 install numerai-cli

# initialize the CLI with API keys and a config folder
numerai setup

# copy a python example and configure a Prediction Node 
numerai node config --example tournament-python3

# build and deploy a docker container to AWS
numerai node deploy

# trigger your compute node in AWS and monitor it
numerai node tes
```

## Timing <a id="getting-started"></a>

The webhook url assigned to your Prediction Nodes are automatically registered with your Numerai Models. Numerai will execute those webhooks on Saturday at 19:00 UTC \(an hour after the round starts\). If we haven't successfully received submissions from your models by Sunday 2:00 UTC, we will email you a warning that it looks like your compute jobs have failed. If any failed, we will try to trigger those webhooks again on Sunday 19:00 UTC and if any fail again, we will send out a final email on Monday 2:00 UTC.

## Upgrading

The newest version of the CLI changes the configuration format that is not backwards compatible with 0.1 and 0.2 versions of the CLI. Upgrading to the new version is simple:

```text
pip3 install --upgrade numerai-cli --user
numerai upgrade
```

## Help <a id="getting-started"></a>

Follow our step by step [tutorial](https://docs.numer.ai/help/compute-tutorial) or watch the video on [YouTube](https://youtu.be/-3y0N7fqfOI) for help updating to 0.3.0.

Ask for help in the [\#Compute RocketChat channel](https://community.numer.ai/channel/compute).



