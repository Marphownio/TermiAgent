**The description of current metasploit exploit**
This module detects VxWorks and the IPnet IP stack, along with devices          vulnerable to CVE-2019-12258.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/vxworks/urgent11_check
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORTS – default: 21 22 23 80 443 - Target ports for TCP detections

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.