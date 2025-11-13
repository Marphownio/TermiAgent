**The description of current metasploit exploit**
This module exploits an authentication bypass vulnerability in Telerik Report Server versions 10.0.24.305 and          prior which allows an unauthenticated attacker to create a new account with administrative privileges. The          vulnerability leverages the initial setup page which is still accessible once the setup process has completed.          If either USERNAME or PASSWORD are not specified, then a random value will be selected. The module will fail if          the specified USERNAME already exists.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/telerik_report_server_auth_bypass
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 83 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.