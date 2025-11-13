**The description of current metasploit exploit**
Wordpress plugin Easy WP SMTP versions <= 1.4.2 was found to not include index.html within its plugin folder.          This potentially allows for directory listings.  If debug mode is also enabled for the plugin, all SMTP          commands are stored in a debug file.  An email must have been sent from the system as well to create the debug          file.  If an email hasn't been sent (Test Email function not included), Aggressive can bypass the last check.          Combining these items, it's possible to request a password reset for an account, then view the debug file to determine          the link that was emailed out, and reset the user's password.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wp_easy_wp_smtp
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 80 - The target port (TCP)
* TARGETURI – default: / - The base path to the wordpress application

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.