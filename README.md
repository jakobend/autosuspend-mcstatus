# autosuspend-mcstatus

This Python package provides [mcstatus](https://github.com/Dinnerbone/mcstatus)
integration for [autosuspend](https://github.com/languitar/autosuspend).

## Quickstart

To suspend your server when no players are online on the local Minecraft server
add the following section to your `autosuspend.conf`:
```ini
[check.Minecraft]
class = autosuspend_mcstatus.PlayersOnline
enabled = true
```

## Documentation

Configuration options for all checks:
```ini
# Address of your Minecraft server. Port is optional if it is 25565 or a SRV record is set.
# Defaults to localhost:25565.
server = example.com:12345
# Number of retries before a query fails.
# Defaults to 3.
retries = 3
```

### `autosuspend_mcstatus.ServerOnline`

Suspends if the server is not running or cannot be reached.

### `autosuspend_mcstatus.PlayersOnline`

Suspends if less than or equal to `treshold` players are on a server, or if the
server cannot be reached.

Configuration options:
```ini
# Number of players below or equal to which suspending will be allowed.
# Defaults to 0.
treshold = 0
```
