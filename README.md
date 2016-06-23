redis-monitor-list
===

A small script that checks the size of a list. Runs `llen`
on the provided selected list and returns the result to
stdout.

Installation
---

**From Source**

```sh
~ # git clone https://github.com/thejpanganiban/redis-monitor-list
~ # cd redis-monitor-list
~/redis-monitor-list # pip install -r requirements.txt 
~/redis-monitor-list # ./monitor_list.py
```

Usage
---

*The command*
```
Usage: python monitor_list.py [list]
```

*Fetching a list size*
```
~ # python monitor_list.py mylistasqueue
23  # We have 23 items in mylistasqueue
```

Configuration
---

The `monitor_list.py` script picks-up configuration from
the environment. Here are the environment variables it
uses and their defaults.

### REDIS_HOST

*Default: 127.0.0.1*

Which redis host to check against.

### REDIS_PORT

*Default: 6379*

Port of which redis is exposed.

### REDIS_DB

*Default: 0*

The db instance to check against.

Advanced Usage
---

TODO
