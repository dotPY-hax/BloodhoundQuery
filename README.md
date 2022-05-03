# BloodhoundQuery
A little program to parse and query Bloodhound data

Inspired by Ippsecs video https://www.youtube.com/watch?v=o3W4H0UfDmQ and the horrible UI of jq I decided to make my own program with even worse UI. Its meant for getting simple data from Bloodhound.zip so you dont have to run Bloodhound just to list some user names.

When run without the `-i` parameter you get premade lists of queries.

This whole thing is very much WIP and might or might not die in side-project hell. If I decide to continue this there will be SQL support at some time as well as better UI code.

```
usage: bloodhound_query.py [-h] [-f F] [-i]

options:
  -h, --help  show this help message and exit
  -f F        Path to BloodHound.zip
  -i          Opens interactive mode which lets you parse the data by hand.
