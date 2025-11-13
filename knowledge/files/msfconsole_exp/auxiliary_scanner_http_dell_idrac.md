**The description of current metasploit exploit**
This module attempts to login to a iDRAC webserver instance using        default username and password.  Tested against Dell Remote Access        Controller 6 - Express version 1.50 and 1.85,        Controller 7 - Enterprise 2.63.60.62        Controller 8 - Enterprise 2.83.05        Controller 9 - Enterprise 4.40.00.00

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/dell_idrac
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 443 - Default remote port

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.