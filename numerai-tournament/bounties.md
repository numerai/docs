---
description: Help us improve Numerai and earn NMR!
---

# Bounties

We need and want your help to improve Numerai so we will aim to be clear and fair with our bounties. The examples listed below are not exhaustive and the bounty amounts are only rough guidelines - the exact amounts depends on the impact and the difficulty of the bug, feedback or exploit. **Actual bounties paid, if any, will be determined by Numerai at its sole discretion.**

Please allow 3-5 business days for a response to reports and an additional 7-10 business days to resolve any reports. We kindly ask for your patience - we are a small team and must prioritize large, high-impact projects - please do not follow up more than once about a report.

{% hint style="warning" %}
You must have a [Numerai Tournament](https://numer.ai/tournament/) account to receive bounty payment. US persons receiving a bounty valued > $600 USD will be required to submit [W9 taxpayer information](broken-reference/). **Regardless of your tax jurisdiction, you are solely responsible for any tax implications related to any bounty payouts you may receive.**
{% endhint %}

## Bugs

If you see anything that is broken, report it! If it turns out to be a real issue and your report helped us fix it then we will give you a bounty:

<table><thead><tr><th width="365">Bug report</th><th>Bounty</th></tr></thead><tbody><tr><td>Small website display / styling issues, broken emails, broken links, typos</td><td>0.1-1 NMR</td></tr><tr><td>Incorrect data / scoring / payouts or broken services (e.g. cannot submit / stake)</td><td>1-5 NMR</td></tr></tbody></table>

## Security Exploits & Vulnerabilities

At Numerai, we take security very seriously, but we are also a small team and place an emphasis on priority, severity, and impact of exploits & vulnerabilities:

| Vulnerability Report                                                                                                    | Bounty     |
| ----------------------------------------------------------------------------------------------------------------------- | ---------- |
| Low-impact exploits & vulnerabilities that cannot risk funds of Numerai or its users                                    | 0.1-2 NMR  |
| Moderate-impact exploits & vulnerabilities that could risk funds of Numerai or its users in some circumstances          | 2-10 NMR   |
| High-impact exploits & vulnerabilities that easily risk funds of Numerai or its users                                   | 10-100 NMR |
| Significant security risks that could risk all funds of our Numerai and it's stakers, effectively ending the tournament | 100+ NMR   |

Before you start researching, we'd like to ask you to refrain from the following while you research:

* Spamming, Denial of service, or other impacts to Numerai's production services
* Rate limiting attacks (unless there is a very low bar and it constitutes a significant risk)
* Attacking or compromising other users accounts
* Publicly disclosing the exploit or vulnerability

### High Priority

We consider the following to be serious security concerns:

* Gaining access to User accounts without direct action from the user
* Compromising API tokens, website credentials, or other sensitive information
  * When reporting credentials leaks, the leaked credentials must contain a valid email / password combination that can be used to login to an existing Numerai account.
  * To submit these credentials, please include a valid CSV file with columns \["email", "password"]. We will not be able to accept or verify credentials submitted any other way.
  * Reward amounts for this kind of report are based on the following criteria:
    * If you cannot actually steal NMR from the account, this is considered "low impact" and you will recieve 0.1 NMR per leaked account.&#x20;
    * If you **can** steal the NMR from the account, we will pay you up to the full stake in the account
* Loss of funds for Numerai or its users that involve no interaction from Numerai or its users
* Gaining access to or control of Numerai's production services with no interaction from Numerai
* Exploits of any Numerai tournament that could lead to unintended payouts
* Subdomain takeovers - please demonstrate that you are able to take over the page by leaving a non-offensive message, such as your username

Generally, we will resolve the above within 3-5 business days and the bounty will on the higher end.

### **Low Priority**

We consider the following to be of negligible security impact. We ask that researchers generally refrain from reporting these unless their is a clear and significant exploit that can be easily used to cause a high impact. Researchers must provide a concrete explanation as to how these vulnerabilities could be used to harm Numerai and it's users as well as a valid proof-of-concept to harness the exploit:

* Vulnerabilities as reported by automated scanners / tools (Acunetix, Vega, OSINT Framework, etc.) without a clear and significant exploit.
* Vulnerabilities in the form of missing configurations / certificates that cannot be easily used to harm Numerai or its users:
  * Missing security headers
  * SSL/TLS scan reports (such as SSL Labs)
  * Missing DNS configurations / certificates
  * Open ports
  * Unchained open redirects
  * Protocol mismatch
  * Rate limiting
  * Exposed login panels
  * Dangling IPs
  * Missing cookie flags on non-authentication cookies
  * Cross-site Request Forgery (CSRF) with minimal security implications (Logout CSRF, etc.)
* Vulnerabilities citing disclosure of some internal structure that could be used for a theoretical attack without concrete proof of an actual attack:
  * Stack traces
  * Path disclosure
  * Directory listings

Generally, these may take as long as 5-20 business days to resolve depending on the severity and the bounty range will likely be on the lower end.

### **No Priority / Out-of-Scope**

Do not submit the following as examples of vulnerabilities. We do not consider these to be vulnerabilities and reports citing these will not be eligible for a bounty:

* Reports that are highly speculative or reference theoretical damage without a clear proof-of-concept with a step-by-step guide showing how to easily use an exploit.
* Vulnerabilities that cannot be used to easily exploit Numerai or other users of Numerai (e.g. self-xss or having a user paste JavaScript into the browser console are not valid exploits).
* Concerns about best practices / industry standards - while we agree it's necessary to implement security best practices in the long-term, these are usually not primary attack vectors and we are only concerned with ways to compromise accounts, user funds, sensitive data, etc.
* Vulnerabilities only affecting outdated user agents / app versions - we only consider exploits in the latest browser versions for Safari, FireFox, Chrome, Edge, IE,  etc.
* Errors, error messages, or stack traces that:
  * are from 500 internal server errors
  * do not disclose sensitive information
* Password policies and/or brute force password attacks
* Brute-force attacks of any kind that don't circumvent our rate limits
* User enumeration that doesn't circumvent our rate limits
* Signing up with a "victim" email to block that email from creating an account
* Signing up with an email alias
* Uploading non-executable files (CSVs, images, parquet, etc.) through our API
* Downloading public files (CSVs, images, parquet, etc.) listed in our API
* Excess / junk data storage (e.g. old uploads of any kind)
* Sending tokens to trusted third-parties (Google Analytics, etc.)
* Public URLs that are randomly generated and non-guessable
* Information from non-sensitive public APIs used in Numerai's public websites such as the APIs serving numer.ai, signals.numer.ai, crypto.numer.ai, forum.numer.ai, etc.&#x20;
  * This includes GraphQL introspection.
* Lack of password re-input for actions that already require authentication
* Significant lapse in user judgement:
  * Following user-driven links (e.g. users bio links, forum post links, etc.)
  * Gaining physical access to a victim’s computer/device
  * Phishing, social engineering, or public computer concerns
* Our Forum:
  * Using basic HTML tags such as headers (\<h1>) or anchors (\<a>) on our forum
  * Any security issues with the Numerai Forum - we use the Discourse platform, so any security issues should be logged with them. See [here](https://github.com/discourse/discourse/security) for details.

### How to report Exploits & Vulnerabilities

Reports must include:

* An explanation of the exploit or vulnerability.
* The concrete impact this could have on Numerai or its users.
* A discussion on how easily this exploit or vulnerability could be used.
* A step-by-step guide on how to execute an attack.
* A proof-of-concept video showing how the attack would work (if the attack impacts production services or users other than yourself, the report will be ineligible for a bounty)

Once you have compiled your report, send an email to <mark style="color:blue;">security@numer.ai</mark> with the subject "\[Security Report] Short Title of Report" where "Short Title of Report" is a clear and concise name for the exploit or vulnerability.

### How to give feedback and suggestions

Message us on the [Discord](https://discord.gg/numerai).

If you are going for a large bounty, it would be helpful if you wrote up your idea in a document (pdf or google docs) or a notebook (google colab, github).
