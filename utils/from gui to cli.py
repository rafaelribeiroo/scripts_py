from gi import require_version
require_version('Gdk', '3.0')
require_version('Gtk', '3.0')
from subprocess import check_output, CalledProcessError
from time import strftime, sleep
from gi.repository import Gdk
from os import environ


def run_cmd(cmdlist):
    """ Reusable function for running external commands """
    new_env = dict(environ)
    new_env['LC_ALL'] = 'C'
    try:
        stdout = check_output(cmdlist, env=new_env)
    except CalledProcessError:
        pass
    else:
        if stdout:
            return stdout


def print_info(stack, event):
    base_xprop = ['xprop', '-notype']
    for xid in stack:
        pid = None
        check_pid = run_cmd(base_xprop + ['_NET_WM_PID', '-id', str(xid)])
        if check_pid:
            pid = check_pid.decode().split('=')[1].strip()
        with open('/proc/' + pid + '/cmdline') as fd:
            command = fd.read()
        print(strftime("%d %H:%M") + event + pid + ' ' + command)


def main():
    sc = Gdk.Screen.get_default()
    old_stack = None

    while True:
        stack = [win.get_xid() for win in sc.get_window_stack()]
        if old_stack:
            # Difference between current and old stack will show new programs
            diff = set(stack) - set(old_stack)
            if diff:
                print_info(diff, " 'New window open' ")
        else:
            print_info(stack, " 'Script Started' ")

        old_stack = stack
        sleep(2)


if __name__ == '__main__':
    main()
