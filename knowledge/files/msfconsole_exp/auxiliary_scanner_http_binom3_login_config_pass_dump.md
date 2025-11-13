**The description of current metasploit exploit**
This module scans for Binom3 Multifunctional Revenue Energy Meter and Power Quality Analyzer          management login portal(s), and attempts to identify valid credentials.          There are four (4) default accounts - 'root'/'root', 'admin'/'1', 'alg'/'1', 'user'/'1'.          In addition to device config, 'root' user can also access password file.          Other users - admin, alg, user - can only access configuration file.          The module attempts to download configuration and password files depending on the login user credentials found.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/binom3_login_config_pass_dump
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
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