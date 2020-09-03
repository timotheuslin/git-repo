# Using Repo in Microsoft Windows

Only Windows 10 is supported and tested.


## Launch Repo from the Windows command prompt (option 1)

* Open the Start Menu (i.e. press the ⊞ key).
* Type cmd to select "Command Prompt"
* ~~Right click it and select "**Run as administrator**".~~
* Git-Repo.Win32 would elevate the UAC as adim inside the script automaticlly.
* Run repo.cmd with its full path under your designated pull folder.
    * e.g. C:\foo\bar> c:\git-repo\repo.cmd ...
* You may consider adding this git-repo's source direcotry to your **PATH** environment variable. Then you can invoke Repo without the leading directory path.


## Launch Repo from Git Bash (option 2)

If you have Git Bash which comes with the Git installation, you can launch that with appropriate permissions.

* Open the Start Menu (i.e. press the ⊞ key).
* Find/search for "Git Bash".
* ~~Right click it and select "**Run as administrator**".~~
* Git-Repo.Win32 would elevate the UAC as adim inside the script automaticlly.

This environment is only needed when running `repo`, or any specific `git`
command that might involve symlinks (e.g. `pull` or `checkout`).
You do not need to run all your commands in here such as your editor.


## Symlinks with GNU tools

If you want to use `ln -s` inside of the default Git/bash shell, you might need
to export this environment variable:
```sh
$ export MSYS="winsymlinks:nativestrict"
```

Otherwise `ln -s` will copy files and not actually create a symlink.
This also helps `tar` unpack symlinks, so that's nice.


## References

* https://github.com/git-for-windows/git/wiki/Symbolic-Links
* https://blogs.windows.com/windowsdeveloper/2016/12/02/symlinks-windows-10/


## Python

Python 3.6 or newer is required.

Python 2.x is deprecated.

You can download the latest Python3's Windows installer here:<br>
https://www.python.org/downloads/release/python-3

When installing Python, make sure the **[Python Laucher](https://www.python.org/dev/peps/pep-0397/)** is checked.


## Git

You should install the most recent version of Git for Windows:<br>
https://git-scm.com/download/win

When installing Git, make sure to turn on **Enable symbolic links** when prompted.

If you've already installed Git for Windows, you can simply download the latest
installer from above and run it again.


### Git worktrees

**Warning**: Repo's support for Git worktrees is new & experimental.
Please report any bugs and be sure to maintain backups!

The Repo 2.4 release introduced support for [Git worktrees][git-worktree].
You don't have to worry about or understand this particular feature, so don't
worry if this section of the Git manual is particularly impenetrable.

The salient point is that Git worktrees allow Repo to create Repo client
checkouts that do not require symlinks at all under Windows.
This means users no longer need Administrator access to sync code.

Simply use `--worktree` when running `repo init` to opt in.

This does not effect specific Git repositories that use symlinks themselves.

Ref. [git-worktree](https://git-scm.com/docs/git-worktree)


## FAQ

### Repo upload always complains about allowing hooks or using --no-verify!

When using `repo upload` in projects that have custom repohooks, you might get
an error like the following:
```sh
$ repo upload
ERROR: You must allow the pre-upload hook or use --no-verify.
```

This can be confusing as you never get prompted.
[MinTTY has a bug][mintty] that breaks isatty checking inside of Repo which
causes Repo to never interactively prompt the user which means the upload check
always fails.

You can workaround this by manually granting consent when uploading.
Simply add the `--verify` option whenever uploading:
```sh
$ repo upload --verify
```

You will have to specify this flag every time you upload.

[mintty](https://github.com/mintty/mintty/issues/56)


### repohooks always fail with an close_fds error.

When using the [reference repohooks project][repohooks] included in AOSP,
you might see errors like this when running `repo upload`:
```sh
$ repo upload
ERROR: Traceback (most recent call last):
  ...
  File "C:\...\lib\subprocess.py", line 351, in __init__
    raise ValueError("close_fds is not supported on Windows "
ValueError: close_fds is not supported on Windows platforms if you redirect stdin/stderr/stdout

Failed to run main() for pre-upload hook; see traceback above.
```

This error shows up when using Python 2.
You should upgrade to Python 3 instead (see above).

Ref. [repohooks](https://android.googlesource.com/platform/tools/repohooks)
