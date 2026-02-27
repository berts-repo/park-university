# Unit 3: Discussion



**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2024-01-26T00:44:06Z

Class,

I wanted to expand on ACLs and have chosen to explore time-based ACLs, which can be configured to time ranges. Cisco introduced this feature in their 12.0.1.T release, and it allows for the creation of ACL based on the time and day of the week. The time range can use the router clock but works best with NTP.

Here is the syntax:
#time-range <time-range-name>

  #periodic <days-of -the-week hh:mm> to <days-of-week hh:mm>

      or

  #absolute <start time date> <end time date>

 

Example ACL configuration:

#access-list 101 permit permit tcp any host 192.168.1.0 0.0.0.255 eq ssh 22 time-range WEEKENDS

#time-range WEEKDAYS

  #periodic Saturday Sunday 8:00 to 16:30

 

https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html

---
