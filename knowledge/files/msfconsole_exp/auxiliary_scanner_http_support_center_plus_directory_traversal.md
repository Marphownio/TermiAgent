**The description of current metasploit exploit**
This module exploits a directory traversal vulnerability found in ManageEngine          Support Center Plus build 7916 and lower. The module will create a support ticket          as a normal user, attaching a link to a file on the server. By requesting our          own attachment, it's possible to retrieve any file on the filesystem with the same          privileges as Support Center Plus is running. On Windows this is always with SYSTEM          privileges.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/support_center_plus_directory_traversal
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