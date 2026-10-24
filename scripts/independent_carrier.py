#!/usr/bin/env python3
"""Offline independent finite tests for the Seifert-fibred link proof; standard library only.

No author checker is imported or executed. Regions and left/right incidences
are rebuilt from rational polylines for EACH support, using winding signatures
of a forest cycle basis. Rounding uses rational Gaussian elimination; whole
complement widths use a separate A-only-wall propagation on rebuilt A union B.
These are representative-width checks, not an independent proof of the PS
minimum or the 3-manifold isotopy theorem. Only files beside this script are
written. Invoke: python3 -B scripts/independent_carrier.py
"""
from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def point(x, y):
    return F(x), F(y)


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def on_segment(a, b, p):
    return (cross(a,b,p) == 0 and min(a[0],b[0]) <= p[0] <= max(a[0],b[0])
            and min(a[1],b[1]) <= p[1] <= max(a[1],b[1]))


def intersects(a,b,c,d):
    x,y,z,t = cross(a,b,c),cross(a,b,d),cross(c,d,a),cross(c,d,b)
    return (x*y < 0 and z*t < 0) or any((
        x == 0 and on_segment(a,b,c), y == 0 and on_segment(a,b,d),
        z == 0 and on_segment(c,d,a), t == 0 and on_segment(c,d,b)))


def winding(poly, p):
    value = 0
    for a,b in zip(poly,poly[1:]+poly[:1]):
        assert not on_segment(a,b,p)
        orient = cross(a,b,p)
        if a[1] <= p[1] < b[1] and orient > 0:
            value += 1
        if b[1] <= p[1] < a[1] and orient < 0:
            value -= 1
    return value


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for a in range(total+1):
            for tail in compositions(total-a,count-1):
                yield (a,)+tail


class Drawing:
    def __init__(self, name, vertices, positive, paths, cones):
        self.name = name
        self.vertices = {v:point(*p) for v,p in vertices.items()}
        self.positive = frozenset(positive)
        self.edges = {}
        for label,a,b,mids in paths:
            assert a not in self.positive and b in self.positive
            self.edges[label] = (a,b,[self.vertices[a]]+
                                 [point(*p) for p in mids]+[self.vertices[b]])
        self.cones = [(q,point(*p)) for q,p in cones]
        self.region_cache = {}
        self.matching_cache = {}
        self.width_cache = {}
        self.validate()

    def segments(self, support):
        return [(e,i,a,b) for e in sorted(support)
                for i,(a,b) in enumerate(zip(self.edges[e][2],self.edges[e][2][1:]))]

    def validate(self):
        segments = self.segments(self.edges)
        for e,i,a,b in segments:
            assert a != b
            for _,p in self.cones:
                assert not on_segment(a,b,p)
            for f,j,c,d in segments:
                if (e,i) >= (f,j) or not intersects(a,b,c,d):
                    continue
                if e == f:
                    assert abs(i-j) == 1 and set((a,b)) & set((c,d))
                    continue
                common = set(self.edges[e][:2]) & set(self.edges[f][:2])
                shared = set((a,b)) & set((c,d))
                assert shared and shared <= {self.vertices[v] for v in common}, (e,f)
                # Collinear overlap beyond a shared endpoint is prohibited.
                assert not (cross(a,b,c) == cross(a,b,d) == 0), (e,f)
        # Distinct parallel edges must remain distinct proper classes: each
        # side of their two-edge Jordan curve has a marked feature.
        for e,f in combinations(self.edges,2):
            a,b,ep = self.edges[e]
            c,d,fp = self.edges[f]
            if (a,b) != (c,d):
                continue
            poly = ep + list(reversed(fp))[1:-1]
            markers = [p for v,p in self.vertices.items() if v not in (a,b)]
            markers += [p for _,p in self.cones]
            inside = [winding(poly,p) != 0 for p in markers]
            assert any(inside) and not all(inside), (e,f,'isotopic duplicate')

    def matchings(self, support):
        support = frozenset(support)
        if support not in self.matching_cache:
            ans=[]
            for chosen in combinations(sorted(support),len(self.vertices)//2):
                degrees=defaultdict(int)
                for e in chosen:
                    for v in self.edges[e][:2]: degrees[v]+=1
                if all(degrees[v] == 1 for v in self.vertices):
                    ans.append(frozenset(chosen))
            self.matching_cache[support]=ans
        return self.matching_cache[support]

    def regions(self, support):
        support=frozenset(support)
        if support in self.region_cache:
            return self.region_cache[support]
        # Forest paths build a geometric fundamental cycle basis.
        tree=defaultdict(list)
        cycles=[]
        components=len(self.vertices)
        for e in sorted(support):
            a,b,line=self.edges[e]
            q=deque([b]); parent={b:None}
            while q and a not in parent:
                v=q.popleft()
                for w,ee in tree[v]:
                    if w not in parent:
                        parent[w]=(v,ee); q.append(w)
            if a not in parent:
                tree[a].append((b,e)); tree[b].append((a,e)); components-=1
                continue
            steps=[]; v=a
            while v != b:
                prev,ee=parent[v]; steps.append((prev,v,ee)); v=prev
            poly=list(line)
            for u,v,ee in reversed(steps):
                aa,bb,ll=self.edges[ee]
                oriented=ll if (aa,bb)==(u,v) else list(reversed(ll))
                assert poly[-1] == oriented[0]
                poly.extend(oriented[1:])
            assert poly[-1] == poly[0]
            cycles.append(poly[:-1])

        def signature(p):
            return tuple(winding(poly,p) for poly in cycles)

        segments=self.segments(support)
        sides={}; all_faces=set()
        for e in sorted(support):
            edge_sides=[]
            for _,i,a,b in [s for s in segments if s[0] == e]:
                mid=((a[0]+b[0])/2,(a[1]+b[1])/2)
                dx,dy=b[0]-a[0],b[1]-a[1]
                eps=F(1,16)
                while True:
                    probes=[(mid[0]-eps*dy,mid[1]+eps*dx),
                            (mid[0]+eps*dy,mid[1]-eps*dx)]
                    clear=all(not intersects(mid,p,c,d)
                              for p in probes for ff,j,c,d in segments
                              if (ff,j) != (e,i))
                    if clear: break
                    eps/=2
                    assert eps > F(1,2**40)
                edge_sides.append(tuple(signature(p) for p in probes))
            assert len(set(edge_sides))==1, (e,edge_sides)
            sides[e]=edge_sides[0]; all_faces.update(sides[e])
        if not all_faces: all_faces.add(())
        assert len(all_faces)==1+len(support)-len(self.vertices)+components
        cone_faces=[signature(p) for _,p in self.cones]
        assert set(cone_faces) <= all_faces
        ans=(tuple(sorted(all_faces)),sides,cone_faces)
        self.region_cache[support]=ans
        return ans

    def block_width(self, A, B):
        key=(A,B)
        if key in self.width_cache: return self.width_cache[key]
        faces,sides,_=self.regions(A|B)
        graph=defaultdict(list)
        for e in A-B:
            l,r=sides[e]
            graph[r].append((l,1)); graph[l].append((r,-1))
        heights={faces[0]:0}; queue=deque([faces[0]])
        while queue:
            v=queue.popleft()
            for w,d in graph[v]:
                if w in heights:
                    assert heights[w] == heights[v]+d
                else:
                    heights[w]=heights[v]+d; queue.append(w)
        assert set(heights) == set(faces), (A,B,'complete B complement disconnected')
        result=max(heights.values())-min(heights.values())
        self.width_cache[key]=result
        return result

    def solve(self, support, weights, reference, root):
        faces,sides,_=self.regions(support)
        free=[f for f in faces if f != root]
        matrix=[]
        for e in sorted(support):
            l,r=sides[e]
            matrix.append([F(int(f==l)-int(f==r)) for f in free]+[
                weights[e]-int(e in reference)])
        pivot=0; positions=[]
        for col in range(len(free)):
            row=next((i for i in range(pivot,len(matrix)) if matrix[i][col]),None)
            assert row is not None, 'more than one height constant'
            matrix[pivot],matrix[row]=matrix[row],matrix[pivot]
            d=matrix[pivot][col]
            matrix[pivot]=[x/d for x in matrix[pivot]]
            for i in range(len(matrix)):
                if i != pivot and matrix[i][col]:
                    d=matrix[i][col]
                    matrix[i]=[a-d*b for a,b in zip(matrix[i],matrix[pivot])]
            positions.append(pivot); pivot+=1
        for row in matrix[pivot:]:
            assert all(x == 0 for x in row), 'not a circulation'
        u={root:F(0)}
        u.update({f:matrix[positions[i]][-1] for i,f in enumerate(free)})
        return u

    def decode(self, support, weights, reference=None, root=None, certificate=False):
        support=frozenset(support)
        ms=self.matchings(support); assert ms
        faces,sides,_=self.regions(support)
        reference=ms[0] if reference is None else reference
        root=faces[0] if root is None else root
        u=self.solve(support,weights,reference,root)
        cuts=sorted({F(0),F(1)}|{(-x)%1 for x in u.values()})
        probes=sorted({*cuts[:-1],*((a+b)/2 for a,b in zip(cuts,cuts[1:]))})
        outputs=[]; qvalues=[]
        for t in probes:
            q={f:(x+t).__floor__() for f,x in u.items()}
            chosen=set()
            for e in support:
                l,r=sides[e]
                z=int(e in reference)+q[l]-q[r]
                assert z in (0,1)
                if weights[e]==0: assert z==0
                if z: chosen.add(e)
            chosen=frozenset(chosen)
            assert chosen in ms
            outputs.append(chosen); qvalues.append(q)
        for i,j in combinations(range(len(probes)),2):
            assert {qvalues[j][f]-qvalues[i][f] for f in faces} <= {0,1}
            assert self.block_width(outputs[i],outputs[j]) <= 1
        bary=defaultdict(F)
        intervals=[]
        for a,b in zip(cuts,cuts[1:]):
            index=probes.index((a+b)/2)
            m=outputs[index]; bary[m]+=b-a
            intervals.append({'start':str(a),'end':str(b),'matching':sorted(m)})
        assert sum(bary.values())==1
        assert all(sum(c for m,c in bary.items() if e in m)==weights.get(e,0)
                   for e in self.edges)
        if certificate:
            return {'reference':sorted(reference), 'root':root,
                    'potential':[[list(f),str(u[f])] for f in faces],
                    'intervals':intervals,
                    'barycentric_output':serial_bary(bary)}
        return dict(bary),len(probes)


def serial_bary(bary):
    return [{'matching':sorted(m),'weight':str(c)}
            for m,c in sorted(bary.items(),key=lambda x:sorted(x[0])) if c]


def drawings():
    yield Drawing('original_double_lens',
        {1:(0,0),2:(5,0),3:(2,0),4:(7,0)}, {1,2},
        [('e0',3,1,[]),('e1',3,1,[(1,-1)]),
         ('f0',4,2,[]),('f1',4,2,[(6,-1)])],
        [(2,(1,F(-1,4))),(3,(6,F(-1,4)))])
    yield Drawing('new_four_boundary_connected',
        {1:(-2,-2),2:(2,2),3:(2,-2),4:(-2,2)}, {1,2},
        [('bottom0',3,1,[]),('bottom1',3,1,[(0,-3)]),
         ('right',3,2,[]),('top0',4,2,[]),
         ('top1',4,2,[(0,3)]),('left',4,1,[])],
        [(3,(0,F(-9,4))),(2,(0,F(9,4)))])
    yield Drawing('new_six_boundary_chorded_hexagon',
        {0:(0,0),1:(2,0),2:(3,2),3:(2,4),4:(0,4),5:(-1,2)}, {0,2,4},
        [('h01',1,0,[]),('h12',1,2,[]),('h23',3,2,[]),
         ('h34',3,4,[]),('h45',5,4,[]),('h50',5,0,[]),
         ('chord14',1,4,[]),('low01',1,0,[(1,-1)]),
         ('high34',3,4,[(1,5)])],
        [(2,(1,F(-1,4))),(3,(1,F(17,4)))])
    # Independent common bridge plus nested cycles: marks include other
    # actual holes, so no empty two-edge lens is accepted as a new class.
    yield Drawing('new_six_boundary_forced_bridge',
        {0:(-5,0),1:(5,0),2:(-2,0),3:(2,0),4:(7,0),5:(9,0)}, {0,2,4},
        [('outer_up',1,0,[(0,5)]),('outer_down',1,0,[(0,-5)]),
         ('inner_up',3,2,[(0,1)]),('inner_down',3,2,[(0,-1)]),
         ('bridge',5,4,[])],
        [(3,(0,2)),(2,(0,0))])


def run_drawing(g):
    labels=sorted(g.edges)
    full=frozenset(labels)
    allms=g.matchings(full)
    counts=defaultdict(int)
    shared_flows={}
    certificates=[]
    for mask in range(1<<len(labels)):
        support=frozenset(e for i,e in enumerate(labels) if mask>>i & 1)
        ms=g.matchings(support)
        if not ms: continue
        counts['feasible_subgraphs']+=1
        faces,_,_=g.regions(support)
        for a,b in product(ms,repeat=2):
            w={e:F(e in a) for e in labels}
            u=g.solve(support,w,b,faces[0])
            assert all(x.denominator==1 for x in u.values())
            assert max(u.values())-min(u.values())==g.block_width(a,b)
            counts['ordered_pair_comparisons']+=1
        flows=set()
        for nums in compositions(4,len(ms)):
            flows.add(tuple(sum(F(n,4) for n,m in zip(nums,ms) if e in m)
                            for e in labels))
        for a,b in combinations(ms,2):
            flows.add(tuple(F(2,7)*int(e in a)+F(5,7)*int(e in b) for e in labels))
        for wt in sorted(flows):
            weights=dict(zip(labels,wt))
            bary,probes=g.decode(support,weights)
            counts['distinct_graph_flow_samples']+=1
            counts['threshold_probes']+=probes
            for ref in ms:
                other,_=g.decode(support,weights,reference=ref)
                assert bary==other
                counts['reference_comparisons']+=1
            for root in faces:
                other,_=g.decode(support,weights,root=root)
                assert bary==other
                counts['root_comparisons']+=1
            positive=frozenset(e for e in support if weights[e]>0)
            assert bary==g.decode(positive,weights)[0]
            counts['zero_edge_rebuild_comparisons']+=1
            if wt in shared_flows:
                assert bary==shared_flows[wt]
                counts['common_coordinate_face_comparisons']+=1
            shared_flows[wt]=bary
        # All cliques and all denominator-four barycentric coefficients.
        for size in range(1,len(ms)+1):
            for sigma in combinations(ms,size):
                if any(g.block_width(a,b)>1 for a,b in combinations(sigma,2)):
                    continue
                counts['true_simplices']+=1
                for nums in compositions(4,size):
                    expected={m:F(n,4) for m,n in zip(sigma,nums) if n}
                    weights={e:sum(c for m,c in expected.items() if e in m)
                             for e in labels}
                    assert g.decode(support,weights)[0]==expected
                    counts['exact_simplex_recoveries']+=1
    for a,b in combinations(allms,2):
        if g.block_width(a,b) >= 2:
            wt={e:F(int(e in a)+int(e in b),2) for e in labels}
            certificates.append({'input_pair':[sorted(a),sorted(b)],
                'representative_width':g.block_width(a,b),
                'midpoint_decode':g.decode(full,wt,certificate=True)})
    faces,sides,conefaces=g.regions(full)
    return {
        'name':g.name, 'actual_boundaries':len(g.vertices),
        'vertices':{str(v):list(map(str,p)) for v,p in g.vertices.items()},
        'positive_vertices':sorted(g.positive),
        'edges':{e:{'negative':a,'positive':b,'polyline':
                         [list(map(str,p)) for p in line]} for e,(a,b,line) in g.edges.items()},
        'cones':[{'order':q,'position':list(map(str,p)),'region_signature':f}
                 for (q,p),f in zip(g.cones,conefaces)],
        'region_signatures':faces,
        'edge_sides':sides,
        'matching_list':[sorted(m) for m in allms],
        'whole_complement_width_matrix':[[g.block_width(a,b) for b in allms] for a in allms],
        'distance_two_midpoint_certificates':certificates,
        'counts':dict(counts),
    }


def collision_test():
    """Actual band occupation for the double-lens family, including offsets.

    On chosen lifts: h_11 has outside value 0, L=R=-1, and a chosen
    lift along e1/f1 goes from -1 to 0. On e0/f0 it is 0. The difference
    h_M-h_11 is n_M in each complementary chamber. Interpolating those
    functions gives the band height intervals below. The two cone constants
    collide on x=y (mod 1); at zero both collide with the artificial phase cut.
    """
    g=next(drawings()); full=frozenset(g.edges)
    def phase_flow(x,y):
        # e0: outside 0 -> lens x; e1: lens -1+x -> outside 0.
        # The second lens has y instead of x.
        intervals={'e0':(F(0),x),'e1':(x-1,F(0)),
                   'f0':(F(0),y),'f1':(y-1,F(0))}
        cuts=sorted({F(0),F(1),x%1,y%1})
        bary=defaultdict(F); flow=defaultdict(F)
        for a,b in zip(cuts,cuts[1:]):
            r=(a+b)/2
            chosen=frozenset(e for e,(lo,hi) in intervals.items()
                if any(lo < r+k < hi for k in (-1,0,1)))
            assert chosen in g.matchings(full)
            bary[chosen]+=b-a
            for e in chosen: flow[e]+=b-a
        weights={'e0':x,'e1':1-x,'f0':y,'f1':1-y}
        assert all(flow[e]==weights[e] for e in full)
        assert dict(bary)==g.decode(full,weights)[0]
        return bary
    events=[]
    for c in (F(0),F(1,3),F(1,2),F(1)):
        limit=phase_flow(c,c)
        records=[]
        for d in (F(1,10),F(1,100),F(1,1000)):
            for sign in (-1,1):
                y=c+sign*d
                if not 0<=y<=1: continue
                bary=phase_flow(c,y)
                difference=sum(abs(bary.get(m,0)-limit.get(m,0))
                               for m in set(bary)|set(limit))
                assert difference<=2*d
                records.append({'epsilon':str(sign*d),'l1_change':str(difference)})
        events.append({'cone_phase_collision':str(c),
            'limit_output':serial_bary(limit),'nearby':records})
    return {'normalised_input_cone_constants':{
        'M00':[0,0],'M01':[0,-1],'M10':[-1,0],'M11':[-1,-1]},
        'convex_cone_constants':['x-1','y-1'],
        'events':events,
        'scope':'Embedded-band subfamily only; not a general PL-family implementation.'}


def main():
    sources=sorted((BASE/'proof').glob('*.md'))
    before={p.relative_to(BASE).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sources}
    result={'status':'passed','independent_from_author_checker':True,
        'arithmetic':'fractions.Fraction and integers',
        'cases':[run_drawing(g) for g in drawings()],
        'constant_collar_collision_tests':collision_test(),
        'source_sha256':before,
        'limitations':[
            'No independent algorithm for arbitrary 3-dimensional isotopy or the PS class minimum.',
            'No inference of a uniform theorem from the tested graphs or cone orders.',
            'The arbitrary intersecting-band PL normaliser is not implemented.',
            'The collision test uses an explicit embedded-band subfamily with no discarded circles.',
            'Region and width algorithms share the input drawing, whose segment embedding is checked exactly.']}
    assert before=={p.relative_to(BASE).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__=='__main__':
    main()
