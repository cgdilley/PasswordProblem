# Description

How many password's fit this rule set? 

- Five characters long
- Must include at least 1 number (10 choices.  0-9)
- Must include at least 1 special character (specifically 10 are available in this)
- Letters are not necessary, but you MAY include capital or lower-case. (52 total characters available).
- 
Keep in mind the characters may be anywhere in the problem.
Passing examples:

```
Aab1!
!!!!1
zZ1!Z
1234!
```

# Solution

This solution finds all possible valid sequences of letters, numbers, and special characters, treating them as 
3 distinct categories.  Once that is calculated, these options are then weighted by the number of actual individual
possibilities for characters within those categories, and those values are then summed to get the total.

The different character categories, the length of the password, and the password's minimum requirements can be
tweaked by adjusting the values at the beginning of the script.