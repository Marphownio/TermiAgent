**The description of current metasploit exploit**
This module exploits several authenticated SQL Inject vulnerabilities in VICIdial 2.14b0.5 prior to          svn/trunk revision 3555 (VICIBox 10.0.0, prior to January 20 is vulnerable).          Injection point 1 is on vicidial/admin.php when adding a user, in the modify_email_accounts parameter.          Injection point 2 is on vicidial/admin.php when adding a user, in the access_recordings parameter.          Injection point 3 is on vicidial/admin.php when adding a user, in the agentcall_email parameter.          Injection point 4 is on vicidial/AST_agent_time_sheet.php when adding a user, in the agent parameter.          Injection point 5 is on vicidial/user_stats.php when adding a user, in the file_download parameter.          VICIdial does not encrypt passwords by default.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/vicidial_multiple_sqli
```

Then set the required options:

```bash
# Required parameters with no default value
set PASSWORD <your valid password here>
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