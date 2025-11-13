**The description of current metasploit exploit**
Joomla versions between 4.0.0 and 4.2.7, inclusive, contain an improper API access vulnerability.          This vulnerability allows unauthenticated users access to webservice endpoints which contain          sensitive information. Specifically for this module we exploit the users and config/application          endpoints.          This module was tested against Joomla 4.2.7 running on Docker.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/joomla_api_improper_access_checks
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