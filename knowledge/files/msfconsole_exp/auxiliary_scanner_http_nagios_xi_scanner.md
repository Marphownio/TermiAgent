**The description of current metasploit exploit**
The module detects the version of Nagios XI applications and        suggests matching exploit modules based on the version number.        Since Nagios XI applications only reveal the version to authenticated        users, valid credentials for a Nagios XI account are required.        Alternatively, it is possible to provide a specific Nagios XI version        number via the `VERSION` option. In that case, the module simply        suggests matching exploit modules and does not probe the target(s).

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/nagios_xi_scanner
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
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