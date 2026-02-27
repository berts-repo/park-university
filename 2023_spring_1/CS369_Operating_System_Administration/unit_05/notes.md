# Unit 5: Notes

This unit covers user management, including configuration files, and setting up remote logins using key pairs.

Adding users

These days, there are few isolated systems where adding a user is a simple process. Usually the credentials are stored elsewhere so the user can have as much of single sign on experience as possible. So while there are some straightforward ways of adding users to your instance, it’s more important for you to be aware of what files have to change rather than the particular process itself. So for these exercises, we’ll specify new users through GCP, then examine what it does to the system to enable them to log in.

Passwords

Your instance on GCP doesn’t have any passwords set! OMG, that must mean it is wide open and anyone can log in just by trying. Go ahead. See if that will work.

When you get tired of trying, you may wonder how the system is locked down without a password. The answer is by using a public/private key pair.

Public / Private Key Pairs

As a quick review, public key cryptography utilizes two, related keys, one that is private and should be kept as secure as possible, and one that is so public, you can safely give it to anyone, even post it on a billboard or internet. Even knowing the public key doesn’t give an attacker any special knowledge for breaking the private key.

For remote access, this method is far superior to just having a password. Remember looking at your log files a few units ago and seeing all the ssh login attempts? Your instance was under constant attack from all over the Internet. If you only protect your system with passwords, sooner or later one of these guessing attacks is going to guess a password.

By configuring a system to only allow a login with a key pair eliminates these guessing attacks completely. In order for an attacker to gain access, he or she would have to obtain your private key, which is much harder than guessing. Furthermore, if you secure your own private key with a strong password, even if an attacker could get your key, they would not get immediate access to your remote account. 

When you SSH into your instance from the Cloud Console, GCP is generating keys and storing the private key in your browser session, then propagating the public key to the instance. Once that’s in place, then you are able to login without any additional validation. These keys tend to be very short lived.

We’ll see a similar process in assignment 2 as we do this manually and more permanently.

Configuration files 

You’ll be experimenting with adding commands to your various configuration files. These changes won’t be reflected in your running shell until you log in or start another session. Since doing that every time you make a change gets old, there is an easier way – just use the source command. So for example, if you add an alias to the file myconfigs, then you can test it just by typing

source myconfigs
