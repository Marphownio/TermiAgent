**The description of current metasploit exploit**
This module scan for a vulnerability on Microsoft Exchange Server that          allows an attacker bypassing the authentication and impersonating as the          admin (CVE-2021-26855).          By chaining this bug with another post-auth arbitrary-file-write          vulnerability to get code execution (CVE-2021-27065).          As a result, an unauthenticated attacker can execute arbitrary commands on          Microsoft Exchange Server.          This vulnerability affects (Exchange 2013 Versions < 15.00.1497.012,          Exchange 2016 CU18 < 15.01.2106.013, Exchange 2016 CU19 < 15.01.2176.009,          Exchange 2019 CU7 < 15.02.0721.013, Exchange 2019 CU8 < 15.02.0792.010).          All components are vulnerable by default.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/exchange_proxylogon
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