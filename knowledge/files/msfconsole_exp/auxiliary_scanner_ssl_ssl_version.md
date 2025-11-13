**The description of current metasploit exploit**
Check if a server supports a given version of SSL/TLS and cipher suites.        The certificate is stored in loot, and any known vulnerabilities against that        SSL version and cipher suite combination are checked. These checks include        POODLE, deprecated protocols, expired/not valid certs, low key strength, null cipher suites,        certificates signed with MD5, DROWN, RC4 ciphers, exportable ciphers, LOGJAM, and BEAST.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/ssl/ssl_version
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 443 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.