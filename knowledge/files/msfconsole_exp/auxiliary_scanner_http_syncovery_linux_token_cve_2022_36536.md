**The description of current metasploit exploit**
This module attempts to brute-force a valid session token for the Syncovery File Sync & Backup Software Web-GUI          by generating all possible tokens, for every second between 'DateTime.now' and the given X day(s).          By default today and yesterday (DAYS = 1) will be checked. If a valid session token is found, the module stops.          The vulnerability exists, because in Syncovery session tokens are basically just base64(m/d/Y H:M:S) at the time          of the login instead of a random token.          If a user does not log out (Syncovery v8.x has no logout) session tokens will remain valid until reboot.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/syncovery_linux_token_cve_2022_36536
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 8999 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.