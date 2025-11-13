**The description of current metasploit exploit**
This module exploits an information disclosure vulnerability that allows an          unauthenticated user to enumerate users in the /ViewUserHover.jspa endpoint.          This only affects Jira versions < 7.13.16, 8.0.0 <= version < 8.5.7, 8.6.0 <= version < 8.11.1          Discovered by Mikhail Klyuchnikov @__mn1__          This module has been tested on versions 8.4.1, 8.5.6, 8.10.1, 8.11.0

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/jira_user_enum
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