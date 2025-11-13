**The description of current metasploit exploit**
This module checks a range of hosts for the MS12-020 vulnerability.          This does not cause a DoS on the target.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/rdp/ms12_020_check
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 3389 - Remote port running RDP (TCP)
* THREADS – default: 1 - The number of concurrent threads (max one per host)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```

---
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.