#!/usr/bin/env python3
"""Re-run the three independent standard-library diagnostic entry points."""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for name in ('exact_checks.py', 'independent_topology.py', 'independent_carrier.py'):
    subprocess.run([sys.executable, '-B', str(HERE/name)], check=True)
print('All three finite diagnostic programs passed.')
