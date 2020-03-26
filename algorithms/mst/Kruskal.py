from base import *
from VisualizationBase import *

from disjoint_set import DisjointSet


class Kruskal(VisualizationBase):
    ds = DisjointSet()

    def MAKE_SET(self, v):
        #self.ds.make(v)
        self.ds._data[v] = v

    def FIND_SET(self, e):
        return self.ds.find(e)

    def UNION(self, F, e):
        self.ds.union(F, e)

    def alg(self, G):
        F = list(list())
        dbg("list(self.ds) - 0", list(self.ds))
        self.update(F)
        dbg(self.ds._data)
        for v in V(G):
            self.MAKE_SET(v)
            dbg("list(self.ds)", list(self.ds))
        dbg("sets mades")
        dbg("list(self.ds)", list(self.ds))

        dbg("sort edges according to w into a non-decreasing sequence")
        sortedPairs = sorted(G.edges().data(), key=lambda e: e[2]['weight'])
        dbg("sortedPairs", sortedPairs)

        for step, e in enumerate(sortedPairs):
            dbg("e", e)
            fs0 = self.FIND_SET(e[0])
            dbg("fs0", fs0)
            fs1 = self.FIND_SET(e[1])
            dbg("fs1", fs1)
            if fs0 != fs1:
                self.UNION(e[0], e[1])
                F.append(list(e))
                self.update(forest=F, step=step + 1)
        dbg("list(self.ds)", list(self.ds))
        dbg("list(ds.itersets())", list(self.ds.itersets()))
        dbg("F", F)
        list(self.ds)

#
