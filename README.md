# Suki
Suki is a Python package manager created to make file organization more easily accessible. Suki uses symbolic links and `requirements.txt` to locate your site-packages, gather the information, and add the appropriate files in your current working directory under a special directory called `suki_pkgs`.

This structure is similar to how to npm or yarn handle `node_modules` but allows the user to maintain and edit their packages without ever needing to leave their current working directory.

You can install this CLI tool using pip:
```bash
pip install suki
```

### Example
At the moment, Suki only locates, aggregates, and links all of your project's site-packages. This is useful if you need to make alterations or monitor your site-packages in the local directory. All changes to the site-packages will immediately take effect in the installed packages (thanks to the symbolic link).
```bash
suki -l
```

You can also input the location of the required packages using the `-f` flag:
```bash
suki -l -f "/home/suki/packages/requirements.txt"
```

One thing to remember, the `suki_pkgs` will be dumped in whatever directory you are currently working in.