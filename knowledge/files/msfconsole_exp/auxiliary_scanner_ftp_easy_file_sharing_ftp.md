**The description of current metasploit exploit**
This module exploits a directory traversal vulnerability found in Easy File Sharing FTP Server Version 3.6 and Earlier.          This vulnerability allows an attacker to download arbitrary files from the server by crafting          a RETR command that includes file system traversal strings such as '../'

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/ftp/easy_file_sharing_ftp
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 21 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.