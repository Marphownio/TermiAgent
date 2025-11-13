**The description of current metasploit exploit**
Collect any leaked internal IPs by requesting commonly redirected locations from IIS.          CVE-2000-0649 references IIS 5.1 (win2k, XP) and older.  However, in newer servers          such as IIS 7+, this occurs when the alternateHostName is not set or misconfigured. Also          collects internal IPs leaked from the PROPFIND method in certain IIS versions.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/iis_internal_ip
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

---
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.