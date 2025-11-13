**The description of current metasploit exploit**
This module attempts to enumerate users on the Synology NAS          by sending GET requests for the forgot password URL.          The Synology NAS will respond differently if a user is present or not.          These count as login attempts, and the default is 10 logins in 5min to          get a permanent block.  Set delay accordingly to avoid this, as default          is permanent.          Vulnerable DSMs are:          DSM 6.1 < 6.1.3-15152          DSM 6.0 < 6.0.3-8754-4          DSM 5.2 < 5.2-5967-04

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/synology_forget_passwd_user_enum
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 5000 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.