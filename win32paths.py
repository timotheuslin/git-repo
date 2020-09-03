""" whereis """

__all__ = ["whereis", "whereis_git_exe", "whereis_gpg_exe"]

import os

def whereis(fn, known_dir=None):
    """locate a specified executable's path"""
    ps = os.environ.get('PATH', '').split(os.pathsep)
    if isinstance(known_dir, list):
        ps += known_dir
    for p in ps:
        ret = os.path.join(p, fn)
        if os.path.exists(ret):
            return ret
    return ''

_pf = os.environ.get('ProgramFiles', '')
_pfx86 = os.environ.get('ProgramFiles(x86)', '')

win32_git_dir_candidates = [
    f'{_pf}\\Git\\cmd',
    f'{_pf}\\Git\\bin',
    f'{_pfx86}\\Git\\cmd',
    f'{_pfx86}\\Git\\bin',
]

win32_gpg_dir_candidates = [
    f'{_pfx86}\\GnuPg\\bin',
    f'{_pf}\\GnuPg\\bin',
    f'{_pf}\\Git\\usr\\bin',
    f'{_pfx86}\\Git\\usr\\bin',
]

def whereis_git_exe():
    """locate GIT executable's path"""
    return whereis('git.exe', win32_git_dir_candidates)

def whereis_gpg_exe():
    """locate GPG executable's path"""
    return whereis('gpg.exe', win32_gpg_dir_candidates)
