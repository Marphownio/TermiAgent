**The description of current metasploit exploit**
This module exploits an authentication bypass in libssh server code          where a USERAUTH_SUCCESS message is sent in place of the expected          USERAUTH_REQUEST message. libssh versions 0.6.0 through 0.7.5 and          0.8.0 through 0.8.3 are vulnerable.          Note that this module's success depends on whether the server code          can trigger the correct (shell/exec) callbacks despite only the state          machine's authenticated state being set.          Therefore, you may or may not get a shell if the server requires          additional code paths to be followed.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/ssh/libssh_auth_bypass
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