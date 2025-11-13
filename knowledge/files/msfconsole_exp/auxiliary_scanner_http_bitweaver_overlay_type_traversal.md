**The description of current metasploit exploit**
This module exploits a directory traversal vulnerability found in Bitweaver.          When handling the 'overlay_type' parameter, view_overlay.php fails to do any          path checking/filtering, which can be abused to read any file outside the          virtual directory.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/bitweaver_overlay_type_traversal
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

---
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.