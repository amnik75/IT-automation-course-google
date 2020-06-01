#!/usr/bin/env python3
import sys,subprocess,os

# capture_output only work in pythom3.7 and more. It captures the output and do not show on screen
result = subprocess.run(['ls','.'],capture_output=True)
print(result.stdout.decode())
print(result.stderr.decode())

result = subprocess.run(['sleep','2'])
print(result.returncode)
ar = sys.argv[1]
if ar == 0:
    sys.exit(0)
else:
    sys.exit(1)

my_env = os.environ.copy()
my_env['PATH'] = os.pathsep.join(['/bin/',my_env['PATH']])
result = subprocess.run('myapp in /bin/',env=my_env)