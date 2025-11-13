**The description of current metasploit exploit**
This module uses a malformed packet or timing attack to enumerate users on          an OpenSSH server.          The default action sends a malformed (corrupted) SSH_MSG_USERAUTH_REQUEST          packet using public key authentication (must be enabled) to enumerate users.          On some versions of OpenSSH under some configurations, OpenSSH will return a          "permission denied" error for an invalid user faster than for a valid user,          creating an opportunity for a timing attack to enumerate users.          Testing note: invalid users were logged, while valid users were not. YMMV.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/ssh/ssh_enumusers
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 22 - The target port

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.