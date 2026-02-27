# Unit 7: Discussion



**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2024-02-22T05:09:45Z

Class,

For this week’s discussion I wanted to play around with Ansible. I figured out how to configure Ansible to ping a list of sites. This could be set up, so each node sends out a ping, to each configured IP-address. For example, how we had to ping each device from each PC in last week’s packet tracer. The process could be streamlined making it easier to ping all the IP-addresses in the network, which would make it easier to troubleshoot.

Here are the steps I took:

1) I installed Ansible on Windows Subsystem for Linux (WSL), which requires some prerequisites, and is in the documentation.

2) I then created a directory and moved into that location

3) Then I created the "Inventory" file (.ini) to run from my localhost, which can also be configured as the list of addresses to run the "playbook" from (e.g. each PC in the packet tracer)

Note: ‘[local]’ can be any name, and this is where I would add all the devices I wanted to ping from, by just typing in their IP address or domain name.

4) I then created a playbook (instructions) as a .yml

5) I then ran the playbook with the command: ansible-playbook <name of file>

That’s it!

 

 

Source:

https://docs.ansible.com/ansible/latest/getting_started/index.html

---


### Feedback

**[INSTRUCTOR]:** Excellent.  Creating your own labs is a great way to learn.
