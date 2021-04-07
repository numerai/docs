---
description: This tutorial helps you update Compute to CLI version 0.3.0
---

# Compute Tutorial

[Watch the video on YouTube](https://youtu.be/-3y0N7fqfOI).

IMPORTANT! After you’ve installed the latest version of numerai-cli, use the `--help` flag at any time if you aren’t sure what to do.

![](https://lh4.googleusercontent.com/Z2tOBeUHGNwCv7OCqhiPwEOBQPZxfgQu7vF5hGADFhpw6xKWOa4UaO8EKbCWKveJ4aRgcMHC8OLh-TJvf7qK8epgzAoR9gnNucFAtaUUgv5mWgUsYjsgty-lGj2hgNWklDZy3GwK)

\[00:30\] Open your command prompt and type `pip install --upgrade numerai-cli` then hit ENTER

![](https://lh3.googleusercontent.com/HRyRFQO_wqSoepe037Qs7nFE0oCtqZdKx4t6sKKSab88pLBaUB1rp5890Ajmbd8F_H_4dkO17D_L9YOWFDtsIHzNj39hVXDVdSptsZpgFiPFuB8PLCuuDoL-ul44ZPfOtnsBNUPg)

\[01:09\] Review the available options for CPU cores and RAM by typing `numerai list-constants`then hit ENTER

![](https://lh3.googleusercontent.com/OmyFE37_rGmPSyXfRUmkE8pmPrY7FbnRwqnLFDOoE6FEc8qMU0HpflRjuWVtPPg6jMuricsJpLmKAuB_qyWtTlklcYBrtmbiwuw6vVlmbscz8htV8hgAqpYdtieYGblJBV-ia_1s)

\[02:00\] You must upgrade from within the directory of your previous compute installation. Some people used ‘example-numerai’ so you’ll need to direct your command prompt to that directory. In this case, my compute was installed in C:\Users\Jon\example-numerai so I type: cd C:\Users\Jon\example-numerai

![](https://lh3.googleusercontent.com/tYZ_5X_QRM4XWKpN1A533TjeeCykhv2ESlvLERXRvZ_J69jxk8j13sx5jP-SyFcXx7QyCNgsq7pdcfkeSGDenUQwRjI01kq-h1lcBlqMxdIShHI7MEbitcuf0A5ukSmfWFvTKEac)

\[02:27\] Next, type `numerai upgrade` and hit ENTER

![](https://lh6.googleusercontent.com/jefXvZopiVR5PxvRqrQpog3WbsyiQITlaJdDY2wdCE1VmuT-8ilmAIYZedOeWSbfDborilxs0w9hczIftRzhBgx4cfSD5a6S9SAQYMVVZhriAe-6SA60cbsWoOs-AicvBRfvKifK)

\[03:08\] You’ll be asked if you want to continue. Type `y` and hit ENTER.

![](https://lh4.googleusercontent.com/m871qIYIErv-3pwzGkqcCDHNawfsPiU2ABCpfYqs34x6E4DAtjDopacmoXjRwccFYXVWYe4i3Romb1lLspUeclzAFMn4BSO-NAbXGcXK-Y4en-bFif2afw_J8_uStvGlSBaI55jT)

\[07:27\] After reviewing the available options for numerai node config `--help` we proceed by telling numerai-cli what size preset to use for our node and the path to the folder containing our model. For this example, I type numerai node config -s mem-lg -p C:\Users\Jon\ex-nomi and hit ENTER

When prompted for the model name, be sure that you identify the correct model, as the webhook will be registered to that model name.

Type `your model name` and hit ENTER. For this example, I typed `twitch_example_nomi` and hit ENTER

![](https://lh5.googleusercontent.com/suOSIpGR6_Gk9CIgrmRdQj0RWTgP89Y-gwjz6oI9TpSXEhMTqpm08C7LeOhGm48q_GOho8uFD3gTLHAI-M2P2QGNqPXd5PZPkuG9zi1eZe2fKzkDmTLSouNagcrO7RQpEPcWSIzw)

\[08:48\] Following the success message, numerai-cli recommends to us that we deploy and test the node. Test locally first. Do so by typing `numerai node test -l -v` and hit ENTER

![](https://lh3.googleusercontent.com/H1a0OCVFGzb2NvcIu-IFXs3P-VVB9C1f9YAcFH3XiVbsmBjNM3FWs_mjBECPsNCXwJVk-REOSRgTkWh3iZnjExsTFaa-YuTVOc52gmDD6pFUwbebqnrKTGL_oweeFWG0opzE3IpJ)

\[12:00\] If your local test succeeds, then deploy your mode to AWS. Do so by typing `numerai node deploy` and hit ENTER. Type `your model name` and hit ENTER.

![](https://lh4.googleusercontent.com/-7h0rRCAWppXwC7-cbM9msmJ5iQcmHAz7xUPhPRn0j1FpTPXJ88ffVVqz3zpeLx9jTLnciMynAiMvy1mtKP89MXjsmw_ZyuCtLFTM1CiF051RpRMyMFN5xnGrWf7DSEpgkOt9rWL)

\[12:50\] Once your mode is deployed, do one final test by triggering the webhook. Type `numerai node test -v` and hit ENTER then type `your model name` and hit ENTER.

If your final test was successful, then you are finished! Repeat the node config step for each additional node that you wish to deploy. Enjoy your weekends!  
  


