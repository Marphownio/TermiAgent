**The description of current metasploit exploit**
This module enumerates Apache Tomcat's usernames via malformed requests to        j_security_check, which can be found in the web administration package. It should        work against Tomcat servers 4.1.0 - 4.1.39, 5.5.0 - 5.5.27, and 6.0.0 - 6.0.18.        Newer versions no longer have the "admin" package by default. The 'admin' package        is no longer provided for Tomcat 6 and later versions.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/tomcat_enum
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
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.