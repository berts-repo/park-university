# Unit 4: Discussion

Introduction

This unit’s discussion covers the configuration options available for the nginx web server.

Initial post:

Consider the configuration options for nginx that are  [link: https://nginx.org/en/docs/http/ngx_http_core_module.html] described here. Pick an option that might be useful to your web server, explain what it does, and give an example.

Reply posts:

Respond to two different students, either by adding more description to an option, or by showing how you implemented it on your own web server and what happened when you did.

Directions

Make your initial post by 11:59 PM Wednesday and reply to at least two classmates by 11:59 PM Sunday.

ULOs Reflected In Discussion

Configure nginx web server (CLO 3)

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2023-02-01T21:04:04Z

Class,

I'm going with:

auth_delay time;

this module puts a delay on the attempts allowed when a user enters the wrong username/password. The server will send a 401 Unauthorized response until it accepts the next password, minimizing the amount of attempts made a second in a bruteforce attack.

HTTP is known as a unsecured protocol that encodes the username/passwords in base64 as plaintext under the header "Authorization," so it is susceptible to eavesdropping and man-in-the-middle attacks. HTTPS on the other hand, encrypts its data and uses a secure connection that is established with a certificate. It depends on the amount of traffic and other factors when determining how many seconds you want to re-check authentication but it is recommended to use 1-2 seconds.

To get the auth_delay to work you first have to configure the nginx to compile with the module, by typing this into the shell in the source code directory:

$ ./configure --with-http_auth_request_module

this allows you to add auth_request to the ./configuration, which in turn allows you to implement auth_delay.

---


### Feedback

**[INSTRUCTOR]:** Bert,
Excellent job this week and thanks for getting all your posts in.  As I’ve mentioned before, it really helps to keep the discussion going.  This week we touched on different nginx configuration options (https://nginx.org/en/docs/http/ngx_http_core_module.html).  Thanks for sharing the auth_delay option.  It’s a very interesting one.  You did a great job explaining what it does.  Keep up the great work and don’t hesitate reaching out if you have any questions on any of the material covered.
Prof [INSTRUCTOR]
