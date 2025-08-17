init python 999:
    import os
    import types
    import subprocess

    def privilege_retry(name):
        def wrapper(*args, **kwargs):
            if name in ["open", "_exit"]:
                pass

            try:
                return getattr(os, name)(*args, **kwargs)
            except OSError:
                mas_utils.mas_log.info("[Monika After Story Linux] Attempting to escalate privileges.")

                subprocess.run(['pkexec', '/opt/monika-after-story-linux/resources/scripts/privilege_escalation.sh', name, *args])

        return wrapper

    for name in dir(os):
        if isinstance(getattr(os, name), types.FunctionType):
            setattr(os, name, privilege_retry(getattr(os, name)))