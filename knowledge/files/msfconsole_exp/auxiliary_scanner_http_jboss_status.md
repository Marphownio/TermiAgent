**The description of current metasploit exploit**
This module queries the JBoss status servlet to collect sensitive        information, including URL paths, GET parameters and client IP addresses.        This module has been tested against JBoss 4.0, 4.2.2 and 4.2.3.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/jboss_status
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
set TARGETURI <your JBoss status servlet URI path here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 8080 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.