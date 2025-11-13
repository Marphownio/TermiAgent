**The description of current metasploit exploit**
This module attempts to exploit the directory traversal in the 'locale'        attribute.  According to the advisory the following versions are vulnerable:        ColdFusion MX6 6.1 base patches,        ColdFusion MX7 7,0,0,91690 base patches,        ColdFusion MX8 8,0,1,195765 base patches,        ColdFusion MX8 8,0,1,195765 with Hotfix4.        Adobe released patches for ColdFusion 8.0, 8.0.1, and 9 but ColdFusion 9 is reported        to have directory traversal protections in place, subsequently this module does NOT        work against ColdFusion 9.  Adobe did not release patches for ColdFusion 6.1 or        ColdFusion 7.        It is not recommended to set FILE when doing scans across a group of servers where the OS        may vary; otherwise, the file requested may not make sense for the OS

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/coldfusion_locale_traversal
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
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