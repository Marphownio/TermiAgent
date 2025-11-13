**The description of current metasploit exploit**
This module will test a VNC server on a range of machines and        report successful logins. Currently it supports RFB protocol        version 3.3, 3.7, 3.8 and 4.001 using the VNC challenge response        authentication method.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/vnc/vnc_login
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 5900 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.