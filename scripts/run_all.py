#!/usr/bin/env python3
"""Run thirty-eight standard-library diagnostics; default compares without writes."""
from pathlib import Path
import json
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent
NAMES = ('exact_checks', 'independent_topology', 'independent_carrier',
         'empty_trace', 'multiport', 'independent_empty_trace', 'independent_multiport',
         'geometric_comparison', 'independent_geometry', 'independent_retraction',
         'splice_geometric_comparison', 'independent_splice_geometry',
         'graph_manifold', 'independent_graph_slicing',
         'independent_graph_carrier', 'independent_graph_pl',
         'part7_checks', 'part7_independent_ab', 'part7_independent_wall_phase',
         'part7_independent_potential',
         'part8_checks', 'part8_independent_square', 'part8_independent_extension',
         'part8_independent_pl',
         'part9_checks', 'part9_closure', 'part9_gap_orbits', 'part9_independent',
         'part10_checks', 'part10_independent',
         'part11_star', 'part11_certificate', 'part11_independent',
         'part12_checks', 'part12_common_packet', 'part12_free_returns',
         'part12_independent',
         'part13_hopf12')


def main():
    if any(a != '--update' for a in sys.argv[1:]) or len(sys.argv[1:]) > 1:
        raise SystemExit('Usage: python3 -B scripts/run_all.py [--update]')
    update = '--update' in sys.argv[1:]
    for name in NAMES:
        env = dict(os.environ, PYTHONHASHSEED='0')
        proc = subprocess.run([sys.executable, '-B', str(HERE/(name+'.py'))],
                              cwd=HERE, check=True, text=True, capture_output=True, env=env)
        try:
            data = json.loads(proc.stdout)
        except ValueError:
            data = {'output_lines': proc.stdout.splitlines()}
        canonical = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)+'\n'
        dest = HERE/(name+'.json')
        if update:
            dest.write_text(canonical, encoding='utf-8')
        elif dest.read_text(encoding='utf-8') != canonical:
            raise SystemExit('Report differs: '+name)
        print(name+': passed; '+('stored' if update else 'identical to stored JSON'), flush=True)
    print('All thirty-eight finite diagnostic programs passed.', flush=True)


if __name__ == '__main__':
    main()
