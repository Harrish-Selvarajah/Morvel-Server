# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:27:52 2019

@author: Harrish Selvarajah
"""

from bookLens import bookLens

class NovelFinder:
    
 nl = bookLens()
 datan = nl.loadNovelLensLatestSmall()

 def computesimilarnovel(self, search):
    novels = []
    novelsfound=[]
    for i in range(1, self.datan):
     novels.append(self.nl.novelID_to_name[i])

     
    for i in (name for name in novels if name.startswith(search)):
     novelsfound.append(i.title())
    
    return novelsfound
    
