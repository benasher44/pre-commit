from __future__ import unicode_literals

import shlex

from pre_commit.util import cmd_output


def run_setup_cmd(runner, cmd):
    cmd_output(*cmd, cwd=runner.prefix_dir, encoding=None)


def environment_dir(ENVIRONMENT_DIR, language_version):
    if ENVIRONMENT_DIR is None:
        return None
    else:
        return '{}-{}'.format(ENVIRONMENT_DIR, language_version)


def to_cmd(hook):
    return tuple(shlex.split(hook['entry'])) + tuple(hook['args'])
