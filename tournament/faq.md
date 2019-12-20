# FAQ

#### How many accounts am I allowed to compete with?

You are allowed to compete with up to 3 accounts. Many data scientists use multiple accounts to experiment or compete with different types models. This is fine. In fact, the ability to manage multiple accounts will become a feature on the website eventually.

The purpose of the 3 account limit is to prevent spamming and information attacks. 

Spamming is bad for the tournament as it adds noise and creates a poor UX for everyone else. For example, creating many accounts can take up spots on the leaderboard visually \(even though this does not impact payouts\). This may not always be malicious, but it is clearly negative for everyone else.

Information attacks is the attempt to access information about live targets that is not supposed to be revealed, and thereby gaining an unfair advantage over other competitors. Regardless of how effective this attack is, or how much of an advantage this actually yields, attacks like this is clearly degrades the integrity of the tournament. 

Any user with more than 3 accounts detected will be given notice and 1 week to wind down to 3 accounts. After that, Numerai reserves the right to return any stakes, invalidate any payouts and to ban ALL of the accounts associated with the violator.

#### I lost my MFA device, can you help recover my account?

For security reasons, Numerai will never recover an account that is secured with MFA. This is to prevent others from impersonating and taking over your account. We recognize that this is not the best user experience, but because large amounts of money accounts can hold, we must prioritize security above all else.

Some users choose not to enable MFA at all. This is not recommended as it decreases the security of your account.

In order order to secure your account with MFA but not risk losing your account when you lose your device, you just need to save your recovery codes in a safe place. You can either save it in a password manager or on a piece of paper. 

**What is being predicted?**  
Richard Craib has stated that the training data represents global stock market data.

**Why so vague about what is being predicted?**

Numerai purposely releases very little information about the data in order to maintain the integrity of the tournament. Additionally, the only way to provide hedge-fund quality data for free is to ensure that the data is encrypted and obfuscated. Providing participants with more information only introduces bias and potentially decreases the quality of the predictions submitted.  
****

**Does Numerai trade cryptocurrency?**  
Numerai does not trade cryptocurrency. Further, users are not predicting cryptocurrency prices.   
****

**If I obtain NMR, am I effectively buying into the Hedge Fund?**  
No. Numeraire is an ERC20 utility token. [https://www.cryptoratingcouncil.com/asset-ratings](https://www.cryptoratingcouncil.com/asset-ratings)  
Only institutional and accredited investors can allocate funds to the Hedge Fund for management. Tournament operations and Numeraire are a separate entity from the Hedge Fund.  
****

**Why do I have to stake NMR in order to be compensated?**  
Staking NMR on predictions removes some of the information asymmetry between tournament participants and Numerai. By staking on predictions, users are providing a “costly signal” about the quality of their model \([Spence](https://www.jstor.org/stable/1882010), 1973\). Staking involves risk, which is compensated with NMR for good performance.  
****

**Can I earn NMR any other way?**  
Yes! You can earn NMR by reporting vulnerabilities, creating or contributing to open source packages such as Numerox, translation of technical material to a variety of languages, and other opportunities offered by the team.  
****

**I’m receiving an upload error on the website. How do I fix my CSV file so that it will be accepted?**  
If your prediction file contains parentheses, percentage signs, or spaces then the submission will fail. Remove all special characters and try again. Save yourself some trouble and visit [numer.ai/submit](http://numer.ai/submit) which gives you example code so you can utilize the API and avoid manual submission entirely! For further technical support, reach out at [https://community.numer.ai](https://community.numer.ai).  
****

**I’m receiving an “invalid ID’s” error when I try to upload my submissions. How do I fix my predictions so that my file will be accepted?**  
You are likely trying to upload predictions from the previous round. Make sure that you are using the latest tournament data by downloading the dataset again. Re-run your model with the latest tournament data and you should not receive this error message again.  
****

**I have so many questions that I just don’t know what to do. HELP!!!**  
Please join [RocketChat](https://community.numer.ai) and visit the \#newusers channel. Ask questions and be patient; someone will respond and get you back on track.  
****

**I received a validation correlation score of XX%. Is that good?**  
This is the most difficult puzzle in the world. Models with a given correlation score on the validation data may or may not be performant in the tournament on live data. Your best course of action is to save your production model to stabilize the predictions generated and submit to the tournament every week for several months. Automate your process using Compute so that you don’t have to worry about being on-time. Observe how your model performs relative to other users. After some time has passed and you feel confident in your model, then begin to stake NMR.  
****

**Who controls Numeraire?**  
Numeraire is a decentralized ERC20 token. You can view the smart contract [here](https://etherscan.io/token/0x1776e1f26f98b1a5df9cd347953a26dd3cb46671#readContract) and read the history of the smart contract development [here](https://github.com/numerai/contract).  
  
****

