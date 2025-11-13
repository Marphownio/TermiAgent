**The description of current metasploit exploit**
This module queries the GitLab GraphQL API without authentication          to acquire the list of GitLab users (CVE-2021-4191). The module works          on all GitLab versions from 13.0 up to 14.8.2, 14.7.4, and 14.6.5.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/gitlab_graphql_user_enum
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target hosts here>
set TARGETURI <your target URI here>
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