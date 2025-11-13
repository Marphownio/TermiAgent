**The description of current metasploit exploit**
This module checks for the OpenSSL ChangeCipherSpec (CCS)        Injection vulnerability. The problem exists in the handling of early        CCS messages during session negotiation. Vulnerable installations of OpenSSL accepts        them, while later implementations do not. If successful, an attacker can leverage this        vulnerability to perform a man-in-the-middle (MITM) attack by downgrading the cipher spec        between a client and server. This issue was first reported in early June, 2014.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/ssl/openssl_ccs
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