# SpidERL
Switching between Erlang versions hopefully made easy now.
_Note: not a package manager, you need to manually install your Erlang/OTP versions_

**Please report any bugs in issues.**

# Prerequisites
- Python 3

## Installation

This will create `spiderl` symlink to `/usr/local/bin`, and change the symlink of `erl` and `erlc` to SpidERL.

```sh
git clone https://github.com/robertfiko/spiderl.git
chmod u+x install.py
./install.py
```

To use SpidERL, please make sure that you have `/usr/local/bin` in the correct positon of your PATH.

## Basic usage
**`spider shell` is not so error ressistant yet to typos and bad syntax**
```sh
spiderl shell <version> # starts a shell with the given verison
spiderl local <version> # changes the local config to that version
spiderl gloval <version> # changes the global config to that version
spiderl add <version> <path> # adds a version and its path into config
spiderl update <version> <path> # overwrites a version and its path into config
spiderl remove <version> # TODO
```

```sh
erl # will look for local config, it not found will start the global version
erlc # will look for local config, it not found will start the global version
```

To remove the local config `rm .otp-verison` in your current working directory


## Global Configuration
SpidERL creates a config folder in `~/.config/spiderl`, here there will be two files:
- `otp_version`: this contains the global OTP version, what will be used when no local is specified.
- `otp_paths`: this file follows JSON syntax and matches the version numbers to their `bin` paths. Example:
    ```json
    {
        "22.0": "/path/to/version/22.0/bin/",
        "25.0.3": "/path/to/version/25.0.3/bin/"
    }
    ```

# TODOs:
- add arg check everywhere
- bash scripts a bit redundant
