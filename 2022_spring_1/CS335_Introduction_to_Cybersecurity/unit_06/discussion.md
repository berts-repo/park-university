# Unit 6: Discussion

Introduction

Make your initial post by 11:59 PM Wednesday and reply to at least two classmates by 11:59 PM Sunday. Please keep your posts civil and show respect to your classmates.

Directions

Read the  [link: https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/] OWASP top 10-2017 (Including all the links in the Table of Contents ), and pick one vulnerability that you are especially interested about. Answer the questions in your language: how to determine if a Web application suffers from this vulnerability? How to prevent such a vulnerability. Describe a concrete attack scenario that utilizes this vulnerability. To better understand it, you may need to play around with WebGoat examples and refer to the references in the pdf.

Notice that each vulnerability can only be picked no more than 3 times, i.e., if one vulnerability topic has been picked by three students, you cannot pick it.

Respond to at least two different students. Include any references you find to support or refute another person’s opinions. Just be polite if you disagree.

ULOs Reflected In Discussion

Explain the principles and countermeasures of session hijacking, phishing, and click-jacking. (CLO 2,3)

Explain the media content vulnerabilities and the idea of sandbox. (CLO 2,3)

Explain the idea of privacy attacks and their countermeasures. (CLO 2,3)

Explain and Experiment with cross-site scripting (XSS) and its countermeasures (CLO 3, 4)

Explain and Experiment with cross-site request forgery (CSRF) and its countermeasures (CLO 3, 4)

Explain the principles of remote -file inclusion and local-file inclusion attack. (CLO 2,3)

Explain and Experiment with SQL injection attack and its countermeasures (CLO 3, 4)

Explain the principles of other web server attacks and countermeasures (CLO 2,3)

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2022-02-16T05:41:47Z

Class,

I chose to go with A1:2017-Injection.  Almost any source of data can be a injection vector, and a common web application injection is through HTML injections, often called cross-site scripting (XSS). The preferred method of preventing this vulnerability is using a safe API. (A1:2017-injection) The other methods are to use proper validation for user-inputted data, and properly escaping special characters depending on the interpreter. (A1:2017-injection) 

Popular WordPress plugin Fastest Cache, which has more than a million downloads in October of 2021, could allow access to credentials and admin capabilities by accessing certain sites. The plugin has many vulnerabilities, including SQL injection vulnerabilities, and a XSS bug via a cross-site request forgery (CSRF). 

Work Cited:

A1:2017-injection. OWASP Top Ten 2017 | A1:2017-Injection | OWASP Foundation. (n.d.). Retrieved February 16, 2022, from  [link: https://owasp.org/www-project-top-ten/2017/A1_2017-Injection] https://owasp.org/www-project-top-ten/2017/A1_2017-Injection

Haworth, J. (2021, October 15). Injection vulnerabilities in popular WordPress plugin could expose credentials, allow Admin Access. The Daily Swig | Cybersecurity news and views. Retrieved February 16, 2022, from https://portswigger.net/daily-swig/injection-vulnerabilities-in-popular-wordpress-plugin-could-expose-credentials-allow-admin-access

---
