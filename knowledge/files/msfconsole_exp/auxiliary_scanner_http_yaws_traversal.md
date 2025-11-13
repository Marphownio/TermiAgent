**The description of current metasploit exploit**
This module exploits a directory traversal bug in Yaws v1.9.1 or less.          The module can only be used to retrieve files. However, code execution might          be possible. Because when the malicious user sends a PUT request, a file is          actually created, except no content is written.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/yaws_traversal
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
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