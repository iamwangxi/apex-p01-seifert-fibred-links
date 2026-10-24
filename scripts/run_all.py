#!/usr/bin/env python3
"""Run sixteen standard-library diagnostics; default compares without writes."""
from pathlib import Path
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
NAMES = ('exact_checks', 'independent_topology', 'independent_carrier',
         'empty_trace', 'multiport', 'independent_empty_trace', 'independent_multiport',
         'geometric_comparison', 'independent_geometry', 'independent_retraction',
         'splice_geometric_comparison', 'independent_splice_geometry',
         'graph_manifold', 'independent_graph_slicing',
         'independent_graph_carrier', 'independent_graph_pl')


def main():
    if any(a != '--update' for a in sys.argv[1:]) or len(sys.argv[1:]) > 1:
        raise SystemExit('Usage: python3 -B scripts/run_all.py [--update]')
    update = '--update' in sys.argv[1:]
    for name in NAMES:
        proc = subprocess.run([sys.executable, '-B', str(HERE/(name+'.py'))],
                              cwd=HERE, check=True, text=True, capture_output=True)
        data = json.loads(proc.stdout)
        canonical = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)+'\n'
        dest = HERE/(name+'.json')
        if update:
            dest.write_text(canonical, encoding='utf-8')
        elif dest.read_text(encoding='utf-8') != canonical:
            raise SystemExit('Report differs: '+name)
        print(name+': passed; '+('stored' if update else 'identical to stored JSON'), flush=True)
    print('All sixteen finite diagnostic programs passed.', flush=True)


if __name__ == '__main__':
    main()
