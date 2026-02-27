# Unit 6: Notes

This unit introduces you to installing and configuring a suite of complementary programs. You’ll be building a LEMP server, Linux, (E)nginx, MySQL (MariaDB), and PHP, and then installing a web application that makes use of all these services.

Installing each individual component is fairly simple, but then the trick is getting them all to work together. Fortunately, this is a common stack, so instructions are plentiful.

MySQL vs. MariaDB

For our purposes, these two databases are interchangeable. MariaDB is meant as a binary compatible, drop in replacement for MySQL. For us, that just means that even though we are installing and running MariaDB, the programs that get run on your system are still named mysql and mysqld.

Run a search if want all the gory details, but basically the difference is that MySQL is now owned by Oracle, while MariaDB is managed by an open-source foundation, much like the Mozilla Foundation, which maintains Firefox.

Database access

The backend database server that will run on your system is named mysqld. There is a user interface that can be run on your instance called mysql that will let you interact with the server. This is mostly useful for administrative tasks and isn’t the way most accesses take place.

With a LEMP server, a web user interacts with the nginx server, which passes requests off to the  php server, which makes queries to the database server. The db server then passes results back to the php server, which forwards them to nginx, which then returns them to the web user. Once this process is set up, it usually works smoothly, but you can see how there are quite a few details to get right.

Testing your database

If you want to test your database installation, you might consider looking at installing and configuring a simple database first.

Look at  [link: https://dev.mysql.com/doc/index-other.html] this page and download the world database and setup guide. This will let you work on your instance directly to be  sure that your database is working before you attempt to integrate it with the rest of the stack.
