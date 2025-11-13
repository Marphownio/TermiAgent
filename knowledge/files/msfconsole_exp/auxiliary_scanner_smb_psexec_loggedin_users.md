**The description of current metasploit exploit**
This module uses a valid administrator username and password to enumerate users currently logged in, using a similar technique than the 'psexec' utility provided by SysInternals. It uses reg.exe to query the HKU base registry key.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/smb/psexec_loggedin_users
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 445 - The Target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.