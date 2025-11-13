**The description of current metasploit exploit**
SickRage < v2018-09-03 allows an attacker to view a user's saved Github credentials in HTTP          responses unless the user has set login information for SickRage.          By default, SickRage does not require login information for the installation.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/http_sickrage_password_leak
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 8081 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.