**The description of current metasploit exploit**
This module exploits a directory traversal vulnerability found in Sybase          EAserver's Jetty webserver on port 8000. Code execution seems unlikely with          EAserver's default configuration unless the web server allows WRITE permission.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/sybase_easerver_traversal
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 8000 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.