**The description of current metasploit exploit**
This module will scan for wordpress sites with the Pingback          API enabled. By interfacing with the API an attacker can cause          the wordpress site to port scan an external target and return          results. Refer to the wordpress_pingback_portscanner module.          This issue was fixed in wordpress 3.5.1

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wordpress_pingback_access
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