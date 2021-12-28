# Cowrie (former known as Kippo), https://github.com/cowrie/cowrie


**Introduction:** " Cowrie is a medium to high interaction SSH and Telnet honeypot designed to log brute force attacks and the shell interaction performed by the attacker. In medium interaction mode (shell) it emulates a UNIX system in Python, in high interaction mode (proxy) it functions as an SSH and telnet proxy to observe attacker behavior to another system"

**Worth noticing:**
- Easy to play realtime replay from attackers activity
- Customizable


**Also fits in:** yyy,zzz

**How this tool integrates to our PHR model:** 
With cowrie we try to lure attackers to wrong place, which gives us alert and buys moretime for us to plan our defence and gather threat intelligence 


**Use case:** Using honeytraps to get alerts from outsider on system
On organization system there is multiple honey traps, when any of those are used we start investigation who it is and where it comes. By having good network/system monitoring, we can trace where attacker has been before, what he/she has done on our systems etc. Then we need to decide if we have enough knowledge to block attacker, or wait and try to get more knowledge (Combining IoCs, attackers tehniques, Threat Intelligence), so that we can be sure when we block attacker, he/she doesn't have other ways to get back to our systems    