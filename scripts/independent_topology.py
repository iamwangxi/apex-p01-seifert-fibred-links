#!/usr/bin/env python3
"""Independent, bounded diagnostics. Does not import the author's checker.

The braid orbit consists of genuine embedded arcs on the four-holed sphere:
outer actual boundary, two cone holes x,y, inner actual boundary z.
Only this directory's JSON output is written. No finite check proves the theorem.
"""
from collections import deque
from itertools import product
from math import gcd, prod
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent


def freely_reduce(word):
    stack = []
    for a in word:
        if stack and stack[-1] == -a:
            stack.pop()
        else:
            stack.append(a)
    return tuple(stack)


def inverse(word):
    return tuple(-a for a in reversed(word))


def substitute(word, images):
    return freely_reduce(b for a in word for b in
                         (images[a - 1] if a > 0 else inverse(images[-a - 1])))


def compose(left, right):
    return tuple(substitute(w, left) for w in right)


def syllables(word, orders):
    """Normal form in C_q * C_r * Z, or Z * Z * Z if orders are zero."""
    stack = []
    for a in word:
        factor, exponent = abs(a) - 1, (1 if a > 0 else -1)
        if stack and stack[-1][0] == factor:
            exponent += stack.pop()[1]
        if orders[factor]:
            exponent %= orders[factor]
        if exponent:
            stack.append((factor, exponent))
    return tuple(stack)


def reduce_syllables(word, orders):
    stack = []
    for factor, exponent in word:
        if stack and stack[-1][0] == factor:
            exponent += stack.pop()[1]
        if orders[factor]:
            exponent %= orders[factor]
        if exponent:
            stack.append((factor, exponent))
    return tuple(stack)


def cyclic_word(word, orders):
    w = syllables(word, orders)
    while len(w) > 1 and w[0][0] == w[-1][0]:
        w = reduce_syllables(w[1:] + w[:1], orders)
    if not w:
        return ()
    wi = reduce_syllables(((f, -e) for f, e in reversed(w)), orders)
    return min(t[i:] + t[:i] for t in (w, wi) for i in range(len(t)))


def conjugator_of_z(word):
    """Recover u in image(z)=u z u^-1 for a pure braid automorphism."""
    w = freely_reduce(word)
    prefix = []
    while len(w) > 1 and w[0] == -w[-1]:
        prefix.append(w[0])
        w = w[1:-1]
    assert w == (3,)
    u = tuple(prefix)
    assert freely_reduce(u + (3,) + inverse(u)) == word
    return u


def braid_arc_orbit(depth=6):
    identity = ((1,), (2,), (3,))
    sigma1 = ((1, 2, -1), (1,), (3,))
    sigma1i = ((2,), (-2, 1, 2), (3,))
    sigma2 = ((1,), (2, 3, -2), (2,))
    sigma2i = ((1,), (3,), (-3, 2, 3))
    assert compose(sigma1, sigma1i) == identity
    assert compose(sigma2, sigma2i) == identity
    generators = [compose(s, s) for s in (sigma1, sigma1i, sigma2, sigma2i)]
    for f in generators:
        assert substitute((1, 2, 3), f) == (1, 2, 3)
    moves = [(f, conjugator_of_z(f[2])) for f in generators]
    outer = (-3, -2, -1)

    def closing(w):
        return freely_reduce(outer + w + (3,) + inverse(w))

    seen = {}
    todo = deque([((), 0)])
    while todo:
        w, d = todo.popleft()
        c = closing(w)
        key = cyclic_word(c, (0, 0, 0))
        if key in seen:
            continue
        seen[key] = (w, c, d)
        if d < depth:
            for f, u in moves:
                todo.append((freely_reduce(substitute(w, f) + u), d + 1))

    profiles = []
    for q, r in [(2, 3), (2, 5), (2, 7), (3, 4), (3, 5), (4, 5), (5, 7), (2, 2)]:
        images = {}
        minimum = None
        for ordinary, (w, c, d) in seen.items():
            orb = cyclic_word(c, (q, r, 0))
            assert len(orb) >= 2, (q, r, c, orb)
            assert orb not in images or images[orb] == ordinary, (q, r, c)
            images[orb] = ordinary
            minimum = len(orb) if minimum is None else min(minimum, len(orb))
        profiles.append({'orders': [q, r], 'in_S3_family': gcd(q, r) == 1,
                         'distinct_orbifold_conjugacy_classes': len(images),
                         'minimum_cyclic_syllable_length': minimum})
    # Negative control: the quotient is certainly not injective on arbitrary words.
    assert freely_reduce((1, 1)) != ()
    assert syllables((1, 1), (2, 3, 0)) == ()
    return {'depth': depth, 'embedded_arc_classes': len(seen),
            'maximum_free_word_length': max(len(c) for _, c, _ in seen.values()),
            'profiles': profiles, 'arbitrary_word_negative_control': True,
            'scope': 'pure braid squares on cone/cone/actual holes; endpoint-free arcs'}


def jordan_checks():
    """Use coordinates after eliminating d_n, independently of the t proof."""
    partitions = peripheral_tests = 0
    profiles = [(), (2,), (3,), (4,), (7,), (2, 3), (2, 5), (3, 4), (3, 5)]
    for n in [2, 4, 6, 8]:
        for orders in profiles:
            for a in product([0, 1], repeat=n):
                for eta in product([0, 1], repeat=len(orders)):
                    free = tuple(v - a[-1] for v in a[:-1])
                    torsion = tuple((v - a[-1]) % q for v, q in zip(eta, orders))
                    is_zero = not any(free) and not any(torsion)
                    empty = not any(a) and not any(eta)
                    full = all(a) and all(eta)
                    assert is_zero == (empty or full)
                    partitions += 1
                    for i in range(n):
                        found = []
                        for r in range(-2, 3):
                            df = tuple(-r if i == n-1 else (r if j == i else 0)
                                       for j in range(n-1))
                            dt = tuple((-r if i == n-1 else 0) % q for q in orders)
                            if free == df and torsion == dt:
                                found.append(r)
                        just_i = a[i] == 1 and sum(a) == 1 and not any(eta)
                        except_i = a[i] == 0 and sum(a) == n-1 and all(eta)
                        assert bool(found) == (empty or full or just_i or except_i)
                        assert all(r in [-1, 0, 1] for r in found)
                        peripheral_tests += 1
    return {'partitions': partitions, 'peripheral_tests': peripheral_tests,
            'normal_form': 'Z^(n-1) plus direct sum C_q; eliminate d_n'}


def double_profiles():
    results = []
    for n in [2, 4, 6, 8]:
        for orders in [(), (2,), (3,), (7,), (2, 3), (2, 5), (3, 4), (5, 7)]:
            if n == 2 and not orders:
                continue
            degree = prod(orders)
            # Count directly: 2n-2 genus contribution, and two branched points/order.
            euler = degree * (2 - 2*(n-1)) - sum(2*(degree-degree//q) for q in orders)
            assert euler < 0 and euler % 2 == 0
            results.append({'actual_boundaries': n, 'orders': orders, 'degree': degree,
                            'surface_genus': 1-euler//2})
    return results


def main():
    root = HERE.parent
    source_names = ['proof/objects.md', 'proof/classification.md',
                    'proof/two-boundaries.md', 'proof/vertex-bijection.md',
                    'proof/class-distance.md']
    data = {'status': 'bounded independent diagnostics passed',
            'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'source_sha256': {n: hashlib.sha256((root/n).read_bytes()).hexdigest()
                              for n in source_names},
            'braid_arc_orbit': braid_arc_orbit(),
            'jordan': jordan_checks(),
            'closed_double_profiles': double_profiles(),
            'limitations': ['Does not prove class minimum over arbitrary ambient isotopies.',
                            'Does not prove Schultens Proposition 25 or PS Proposition 3.2.',
                            'No finite enumeration proves exhaustive Seifert classification.',
                            'No author checker was executed or imported.']}
    target = HERE/'independent_topology.json'
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': data['status'], 'braid': data['braid_arc_orbit'],
                      'jordan': data['jordan'],
                      'double_profiles': len(data['closed_double_profiles'])},
                     ensure_ascii=False))


if __name__ == '__main__':
    main()
