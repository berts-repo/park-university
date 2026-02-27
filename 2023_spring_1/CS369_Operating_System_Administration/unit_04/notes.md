# Unit 4: Notes

This unit covers configuring nginx and running multiple static web sites from a single server.

Apache vs. nginx

Nginx and apache are two popular web servers. Apache has a longer history but nginx was designed to handle situations that apache struggles with. The two biggest differences are listed below. First, apache creates a child process to handle every new incoming connection. This is a straightforward model that maximizes use of operating system services.

The downside is that processes require resources, including memory, and when there are thousands of concurrent connections, there may be noticeable degradation in performance. Nginx on the other hand, can manage thousands of connections in a single worker process, which requires far fewer OS resources. Second, apache is designed to be flexible, providing a single web server that can be configured to handle many different situations and many types of dynamic content.

Nginx on the other hand only delivers static content natively, but it does it blazingly fast. Nginx can interact with other processes to handle dynamic web content, but this requires slightly more complicated configuration and interactions.

You can see a little more  [link: https://www.digitalocean.com/community/tutorials/apache-vs-nginx-practical-considerations] detailed summary here. 

Configuration

It’s a good idea to keep a copy of your initial nginx configuration file in a separate location. It’s almost inevitable that you will make some editing change that will break your server’s configuration. If you have a working configuration file, you can compare against it to see what change might be causing the problem.

Enabled vs available web sites

Adding a configuration file in the directory /etc/nginx/sites-available/ only defines a web site on your system. It does not make it active to clients so they can access it. The trick to making the site active is to add a symbolic link to this configuration file in the directory /etc/nginx/sites-enabled.

This may seem unnecessarily complicated at first, but it is a really flexible and elegant solution overall. By keeping /etc/nginx/sites-enabled as symbolic links, you can create and delete these links at will to turn your site on and off, but never actually have to change your actual configuration files.

Port based vs. Domain based web sites 

Normally, when you host multiple web sites on a single server, each would have a different domain name, like  [link: http://www.park.edu] www.park.edu, mypark.park.edu, people.park.edu, etc. When you look at most web server configuration documentation, you’ll see instructions for hosting multiple domains, each one using the default port 80.

However, domain names cost money and there’s no need for you to buy a domain name that you only use for a few weeks. So instead, we’ll use a single IP address, no domain name, and then distinguish between the sites by using different port numbers. The general principle is the same, you just won’t find that many specific documentation examples.
