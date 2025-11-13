# ssh connection
<chunk>

After you have determined the user and password, please log in via ssh in the following format:

```bash
ssh_login --host <target_host> --port <target_port> --user <username> --password <password>
```

### Common Options

| Option           | Description             |
| -----------------|------------------------ |
| `-host`          | target_host             |
| `--port  `       | target_port             |
| `--user  `       | username                |
| `--password`     | password                |

### Example Commands

```bash
ssh_login --host 127.0.0.1 --port 22 --user admin --password admin
```

</chunk>