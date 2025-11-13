**The description of current metasploit exploit**
This module attempts to authenticate to a WinRM service. It currently        works only if the remote end allows Negotiate(NTLM) authentication.        Kerberos is not currently supported.  Please note: in order to use this        module without SSL, the 'AllowUnencrypted' winrm option must be set.        Otherwise adjust the port and set the SSL options in the module as appropriate.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/winrm/winrm_login
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 5985 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.