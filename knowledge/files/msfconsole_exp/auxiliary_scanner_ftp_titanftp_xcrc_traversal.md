**The description of current metasploit exploit**
This module exploits a directory traversal vulnerability in the XCRC command        implemented in versions of Titan FTP up to and including 8.10.1125. By making        sending multiple XCRC command, it is possible to disclose the contents of any        file on the drive with a simple CRC "brute force" attack.        Although the daemon runs with SYSTEM privileges, access is limited to files        that reside on the same drive as the FTP server's root directory.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/ftp/titanftp_xcrc_traversal
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