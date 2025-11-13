**The description of current metasploit exploit**
This module exploits a directory traversal vulnerability found in the WildFly 8.1.0.Final          web server running on port 8080, named JBoss Undertow. The vulnerability only affects to          Windows systems.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wildfly_traversal
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 8080 - The target port (TCP)

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