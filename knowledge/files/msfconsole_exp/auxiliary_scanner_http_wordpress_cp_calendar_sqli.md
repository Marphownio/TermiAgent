**The description of current metasploit exploit**
This module will scan given instances for an unauthenticated SQL injection          within the CP Multi-View Calendar plugin v1.1.4 for Wordpress.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wordpress_cp_calendar_sqli
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host here>
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