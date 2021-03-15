# Compute Tutorial

Compute is a way to automate your weekly submissions to the Numerai Tournament. Learn how to set it up in this tutorial.

_Watch the tutorial video at_ [_YouTube_](https://youtu.be/YFgXMpQszpM)_._

![](https://lh6.googleusercontent.com/JT1YyvA-AYlAGqlIVd-7Vg2NhPuO8rU_hoNX8z1XigAf1PN2ieWIuaBeY_PubKm8kGtMFy09qN_I-pOdtYjK2C9Ab3PO9HvOx3eG_E7y9PCq-WZf7zjWNdy_2eHf4kH2R6A2kPCm)

\(0:24\) Start at your AWS console home page.  
You can access the IAM account control panel by either searching for it like so or by using the pull-down menu \(0:30\)

![](https://lh4.googleusercontent.com/KfbxMlBZWCpxBqCY6Cu1FTXIRhqU81W8efaHRvu8zjVezXGWpQW56g69z-zwBVPXf8kJZj7zA0y0WmKynGBJof_ZN65nuGBpYGLrrQJ9WbttRmpnCmm57Y77b0TgZrccc4VuJXMR)

and clicking on the link.

![](https://lh5.googleusercontent.com/wZI-PSfGNdzSJuGXnOt2GKh3bOqKLvH8MoGcPxxZbfv6u-ysF71iyBjU95Za0P3adHPRWBhZevouhr9JoeOQO-zFX_c_YUlKYvc8Cn5h-uPPoFRVLJAkhbNlSvkYQOjaPwsFuKif)

\(0:36\)

Click users, then click add user. \(0:40\)

![](https://lh3.googleusercontent.com/HHrPPunj5VTQg9tBrVeT0sAzZ48j3M3cRV9sI-jd0W28wiGPVB74CS14nxmxTvWDXS4LF1hc3TX26afnF5yzpjOiWY9BTsqGw-Fy-vCuUmMgwyZXSLHImdepZ_IFujIazDYvVwcl)

Give your new user a name – mine will be numerai\_train. Under access type, click programmatic access, then click next. \(0:50\)

![](https://lh6.googleusercontent.com/UQzDp2KWesCZhe9jb0idCiNI7yszgq3fyYWIldPI-EUx-IGqWW1QgwtU6j24usHJz94j7_7z05rjrGGV_urj1kgZfEXBmFfDMMTFKEtc91cZv1rBiuvvj7R0qJn3XJkXeIgfZ-XE)

Now click attach existing policies directly, and click the first box to grant administrator access. Click next. \(0:58\)

You don’t need to add tags, so click next again. One final click creates your new user. The new user has been created, and the page displays your public key and hides the secret key. I’m going to download the CSV so I can store my numerai API keys as well. \(1:08\)

![](https://lh3.googleusercontent.com/GoNx8KnC6ytT467kMRPLqVKTHV-qHniUolbz3m1lVR3wh2KFN4redjSk7YJKM2jI4UmE_HSMg6VKLCgE_WD11L0VzSfk3TBI9gBdOf-ga6wbjf45yGJ9LMEIn1ym_7wSYylUEriM)

![](https://lh5.googleusercontent.com/6ihfmBIuTe-4BFEUzqwQeQa0v8sMkhrgepSJxQaBQErtNDjAYpjLgXAW2jfHh48xzxmxeae6n6EVeqvcMSePfwyp5LvlCchJkPRuKZfcviyfZ_ZEhXUQ1yAayvQn40UNux_ZcG6h)

Next, open your numerai account settings page and click Add. \(1:31\)

![](https://lh5.googleusercontent.com/zqGTjBjlR_RvBXQlZXhYjVg1bWCHo7BGpqvhjzpZwtbgW2atUE-fIdGK7cP8xe7J2b8n48VOTQ9QSGWB3FBUIdxa7XhWLXcFWAxgFqlHMj2Ub-HFbL7AJPwRj35a78QtGCYvheKN)

Name your key, and check “upload submissions”, “make stakes”, “view historical submission info” and “view user info”. Type in your password, then, click generate key. \(1:48\)

![](https://lh3.googleusercontent.com/ociyl3axYtpsX4Om_2RkV3WjG5xL4UsB-zm7TcGu6S8Y8Ke-ZgFntY-CASfvm5QQ6XBjlsGx_CSYxplgDh7oe_uHJROz2UahQQZLtL7_0U1yhONIvSC84kYre3boOB7v-kwjrRSf)

Copy the secret key which is displayed in the pop-up box in the bottom left corner. \(1:53\)

![](https://lh5.googleusercontent.com/mB9G0owNROjyM0dAU08YCG7qRyJSKVqTpI6HyDpWd4KMB5XG5Dm_v3MMy_mYI0aGVCIQznqYkSYv_3dK2YvRuWcueAy1MVoC80O_2pvCKyooL7KPNCYQVl8_B5N4dGpJlwwsfYcf)

You can save this key in the CSV you downloaded from AWS. Also gather the public key \(2:04\)

_**Note: access and secret keys give control over your AWS and Numerai accounts. Keep them safe like you would usernames and passwords!**_

![](https://lh3.googleusercontent.com/epoIhcwStnpCFXueAGOhZwKmM9-TqLJXCrtLY4cBAUaKSF5wWeh8y32MJGuEyMGUMfft0j5j43oeUHKK9dwUCCFDRa44I4k8Gd5igP49ewR-NEtLQ0DU3aQLGIfUz7k1UUIBMi_J)

Save the public key in the CSV as well. Next, open your anaconda prompt and type `pip3 install numerai_cli`. \(2:23\)

![](https://lh6.googleusercontent.com/zZHb0hph83WJ4ypaUBhmpDu1wHoNXCJKeuVmWswTrweUd2mFJc8zARD8Osis5RcJA3conQOS0kbLSUM-wmCB9hqDoif-lnjDtiwtFQCjrk1mm6QZgBeBtQgv9Y6Fig9l_x0hTP4H)

Once installed, type `mkdir example-numerai`, then `cd example-numerai`, then `numerai setup`. \(2:42\)

![](https://lh4.googleusercontent.com/7_w6V8l6sqcqjPc_XNf1pq3HJmEZwVmg68w4XqoM5i2hrmQXNG2gNXkxDg7aP-Q0vZia_jsaMg8Leg9TddHbq3V56JszLoz3ydGvtsGpuh5CZ92dEK8orM8xNh0efP4_kTt-crnX)

Now, copy and paste the keys as directed by the command prompt. \(3:15\)

![](https://lh4.googleusercontent.com/C0zbxWABUMpQwAsPtMb78XvyfnRa6c4bZT1F4hyvJkA8aFuBuR_hSQv7Pn_xZVMj52grXKaAVxvYeHhPE__NfNk-G7HynDlGuReAqoLDia-lqpSUxNgGC8yXV5YvCU1M8SudPyKS)

You should see a bunch of print messages showing that you’ve successfully installed numerai-cli. \(3:41\)

![](https://lh5.googleusercontent.com/L3DVgnjU_cxeU2Sv7WP-u6gYrPjlgCYuD9hzHlqovS9RdqjeOLISoZ_SyWwFFTj8DIfEcEaeb56CJjas0HE2VgUyZFUpa5kp-Olos6ssUdAxkp923NvITZWo4a6tFH0HsVFklkWK)

Type `numerai docker copy-example`. This gives us all the necessary file names and example code which we can overwrite. \(3:56\)

![](https://lh6.googleusercontent.com/4Z-cFieomwv8gV2d9BtBdltBGsU3Eel9QhYSk01E5h2kIFam5cebN-xAFHIxWw8yjxB6JEnMI45SLbgyPJtyNaxlwyVoCeS6riADOhNm8-Ab399ysh4syyjuvLPKxf-jOnOkUs-v)

Now, I am going to run a very simple regression model using RidgeCV from scikit-learn. We’ll save this model using joblib. Type `numerai docker train`. Docker runs the train.py file, which downloads the data, fits the model, then saves the model using joblib. I’ll spare you the boredom of watching the data download and waiting for the model to train. As you can see, the joblib file has been saved in the example\_numerai folder along with the numerai dataset. \(4:28\)

![](https://lh6.googleusercontent.com/MQayrwIgIVnj-D0JjNUuFDRl1De9GBxvOpwRn5tsz7lr6F7dYlnBgbG5H_xA9U9ZF0HY2AFJyS2YPaEsrLJ5pq7VWVTSkbyrJzSZIh-A5rzYrU3X2-rZ2N61sz4vhg9ebaWeOUt7)

We want to make sure that the model works correctly before we deploy our docker image to AWS. Type `numerai docker run`. This will build the docker image and run predict.py on your machine. Once your model finishes generating predictions, numerox will then upload your predictions using the API keys you provided. \(4:51\)

![](https://lh3.googleusercontent.com/OkYPLYPpsNtp-r15IlxfQOdrpSWuqFVJqwTRZQ8sJ8ZdZkFIiMGSiz6pl3iLIkfDcW4YTVh5QAo8UVnrHrN0FQ6RaXnYUH8mlrGLHFHwx4xbixxw6NyzvCn13xC5hLiaTMRwIbuT)

Let’s gather the webhook address. Navigate to the .numerai folder in the example\_predictions folder. \(4:59\)

![](https://lh3.googleusercontent.com/-qIvZJdaYN-MixvSEDTxFesieZK_cEq8exyzoi8Vh2HH3Ff9TM_wY7qTQ_PFRxeN9PD4kboBFSFr837S1Uwj55hFzCLUnkjmkAGU5CUVBZ_UFzxeTRxDsTtdaLdgtdkLFL_yyskP)

Open submission\_url.txt and copy the address. \(5:03\)

![](https://lh6.googleusercontent.com/-tDzCP5PvZuNDr2KLUswWdNm-SQGsIYFypCaqpkMLMjrV-HYGKal3jH5a75AZ7zBrBKYg5ih7MWCyOdpDWNfJlDpykxyO1pchg8RWUHOJTStos4-MSLRwjyuqim9yVyu29ogk4qC)

Open your numerai account settings once again, click Compute, and paste this address in the field, and click change webhooks. \(5:15\)

![](https://lh3.googleusercontent.com/FIJeEii3ArKQwjrhzkLKniCKSo_KIIYbrB0TFgOad6C6mGhyyY6XJ05jf45sqQ9_w1gqY1BCERnj6LCPx-KKscZDGdMXwpmtyhGCVavoYZzCN3QKs9wyKWgvhz47dyzbxNG_pZNu)

As you can see, the last submission shows that our local test was successful. \(5:23\)

![](https://lh4.googleusercontent.com/Kj7BZsN4ZiJ-3-FUaW9b17PZmAJam6xUJTxKjXzdx9Z3HReUKtdKUr6cghw7i9eV0h1XcEPjV4p5bOwPK6Ao6f-pyltBPs5IEjL0onYprWPyUuSL1NYVhYvcp9SuNAUN6TR6wnYS)

Type `numerai docker deploy` and wait for your docker files to be pushed to AWS. \(5:48\)

![](https://lh3.googleusercontent.com/BknJF6TzVUKr01EnAUA_eeAZQTjxI3UDhaBhyfA_i09DFcRHZrWwWRcjiUzkCXsdK3QuHHk-Qmq9poDBdVvZetql2wo4ecQYSqMH4c-TW-HOq4IOz4mOfscYjsfsvK0pu3jifWqB)

Test the webhook by typing `numerai compute test-webhook`. You can get your logs by typing `numerai compute logs -f`.  


When you see the message “Task is now in the DEPROVISIONING state, your code is finished. \(6:37\)

![](https://lh6.googleusercontent.com/UMDqrC30nc0b8EhpEKK5WilfPFAIj1Jy2T-CJo2PTqtfnzL-inv5TYe6MvQ7lrdCqcvuPH910wRvsmQGl-ZVDHQJd6zPZoWfKLz1wTLY-vEIbyybeCGGg6bWhMGhutEplTwvt-Z8)

_Congratulations, you are now free to enjoy your Saturdays!_

