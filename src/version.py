PROTOCOL_VERSION = 1

def _get_commit_hash():
    import subprocess
    return subprocess.check_output(["git", "show-ref", "HEAD", "-s", "--abbrev"]).strip()

VERSION = _get_commit_hash()
