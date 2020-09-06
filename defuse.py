#################################################Libraries Importation###################################
import gc
import re
import multiprocessing
import inspect
from quality_score import reliability,availibility,reputation,cost
import csv
import math
from formules_saw import quality_score
import time
import itertools
import copy
import numpy as np
from knapsack01 import knapSack

from Service_Lake import *
from criticalpath import Node
import Queue
import glob
import os
from time import sleep
import threading
import time


#Define the structure of a query plan
class Plan:
    count=0
    def __init__(self,incl_services=None,exec_ordering=None,criticalS=None,response_time=None,Ordering_file=None,reliability=None,reputation=None,cost=None,availibility=None,quality_score=None):
        Plan.count+=1
        self.ide= Plan.count
        self.exec_ordering=exec_ordering
        self.incl_services=incl_services
        #self.matchings=matchings
        self.criticalS=criticalS
        self.response_time=response_time
        self.reputation=reputation
        self.reliability=reliability
        self.availibility=availibility
        self.response_time=response_time
        self.cost=cost
        self.quality_score=quality_score

####Construct Combinations and remove duplicates 
def myproduct(*args):
    pools = map(tuple, args)
    result = [[]]
    for pool in pools:
        nresult = []
        for x in result:
            for y in pool:
                if not x+[y] in nresult:
                            nresult.append(list(set(x+[y])))
        result=nresult
        result1=[]
    for el in result:
        if not el in result1:
            result1.append(el)
    return result1

def worker0():
    while True:
        item = conjuncts.get()
        if item is None:
            break
        identify_function(item)
        conjuncts.task_done()
        
def identify_function(conjunct):
    RelevantViews[conjunct[0]]=set()
    for service_view in services_views.keys():
        for parameter in services_views[service_view]:
            if type(parameter[len(parameter)-1])== type(conjunct[len(conjunct)-1]) and parameter[0] ==conjunct[0]:
                i=1
                l=len(parameter)-1
                if l>2:
                    while i<l:
                        map=conjunct[i],'-->',parameter[i]
                        i=i+1
                        RelevantViews[conjunct[0]].update({service_view.ide})
                        Mappings[service_view].update({map})
                else:
                        map=conjunct[1],'-->',parameter[1]
                        RelevantViews[conjunct[0]].update({service_view.ide})
                        Mappings[service_view].update({map})
     

def worker(Res,BindAvail):
    while True:
        item = combinations.get()
        if item is None:
            break
        time_t=time.clock()
        plan,executable=create_function(item,Res,BindAvail)
        if executable:
            evaluate_plan(plan)
        combinations.task_done()
        
def create_function(combination,Res,BindAvail):
    combinations=copy.copy(combination)
    Qout={}
    j=1
    #create the ordering graph
    executable=True
    pred2=''
    predecessors=[]
    valeurs = []
    namep=str("projet")
    p = Node(namep)
    l={}
    while len(combination) > 0 and not BindAvail < Res:
        Exec=[]
        #determine the set of data services which can be executed at iteration i(i.e.,all its required inputs are available)
        for servic in combination:
            for ser in Service_lake:
                if ser.ide==servic:
                    service=ser
            if set(service.inputs).issubset(BindAvail):
                Exec.append(service)
        if not Exec:
            executable=False
        else:
            for service in Exec:
                l[str(service.ide)]=p.add(Node(str(service.ide), duration=int(service.response_time),lag=0))
                predd='"'
                pred2=pred2+service.name+' '+str(service.response_time)+' '
                if len(predecessors)>1:
                    for pr in predecessors:
                        for service1 in Service_lake:
                            if service1.name==pr:
                                p.link(l[str(service.ide)],l[str(service1.ide)])
                                predd=predd+str(service1.ide)+','
                                pred2=pred2+str(service1.name)+' '
                    Index=len(predd)-1
                    Name_list = list(predd)
                    Name_list[Index] = '"'
                    predd = "".join(Name_list)
                elif len(predecessors)==1:
                    for service1 in Service_lake:
                        if service1==predecessors[0]:
                            p.link(l[str(service.ide)],l[str(service1.ide)])
                            predd=str(service1.ide)
                            pred2=pred2+str(service1.name)+' '
                if predd=='"':
                   predd=''
                valeurs.append([str(service.ide),service.name,str(service.response_time),predd,str(0)])
                pred2=pred2+str("\n ")
                for out in service.outputs:
                    BindAvail.add(out)
                combination.remove(service.ide)
        predecessors=[]
        for service in Exec:
            predecessors.append(service)
    if executable:        
        p.update_all()
        s=p.get_critical_path()
        t=p.duration
        time_c=time.clock()
        timeff=timef+time.clock()-time_c
        P=Plan(combinations,pred2,s,t)
        Plans.append(P)
        ii=P.ide
        file=str("Plans/"+"ExecutableOrdering"+str(ii)+".csv")
        f = open(file, 'w')
        ligneEntete = ",".join(entetes) + "\n"
        f.write(ligneEntete)
        n=0
        for valeur in valeurs:
            ligne = ",".join(valeur) + "\n"
            f.write(ligne)
            n+=1
        f.close()
        df = pd.read_csv("Plans/"+"ExecutableOrdering"+str(ii)+".csv")
        for i in range(0,n):
            for servic in P.incl_services:
                if df.at[i,"id"]==servic:
                    for ser in Service_lake:
                        if ser.ide==servic:
                            service=ser
                    p=calls_number(service,str("Plans/"+"ExecutableOrdering"+str(ii)+".csv"))
                    df.at[i, "critical"]= 1
                    df.at[i,"calls_number"]=p
        df.to_csv("Plans/"+"ExecutableOrdering"+str(ii)+".csv", index=False)
        P.Ordering_file=file
    else:
        print("this plan is not executable")
    return P,executable

##determine the QoS values of a plan P
def evaluate_plan(plan):
    plan.cost=cost(str(plan.Ordering_file))
    plan.reputation=reputation(str(plan.Ordering_file))
    plan.availibility=availability(str(plan.Ordering_file))
    plan.reliability=reliability(plan)



##compute the estimated number of web calls
def calls_number(s,P):
    nc=1
    precedents=[]
    with open(P, 'rt') as f2:
        reader = csv.reader(f2) 
        for row in reader:
            if(str(row[1])==s.name):
                precedents=row[3].split(',')
    f2.close()
    if precedents:
        for pred in precedents:
            nc1=1
            avg=1
            for service in Service_lake:
                if str(service.ide)==pred:
                    spred=service
                    nc1=calls_number(spred,P)
                    avg=spred.avg
            nc= nc * nc1 * avg
    s.calls_number=nc
    return nc


##Compute the total execution cost of a service composition
def cost(P):
    cost=0
    with open(P, 'rt') as f2:
        reader = csv.reader(f2) 
        for row in reader:
            for s in Service_lake:
                if(str(row[1])==s.name):
                    cost=cost+s.calls_number * s.cost
        return cost

##Compute the reputation of a service composition
def reputation(P):
    somme = 0 
    n=1
    with open(P, 'rt') as f2:
        reader = csv.reader(f2) 
        for row in reader:
            for s in Service_lake:
                if(str(row[1])==s.name):
                    somme = somme + s.reputation
                    n=n+1
        return (somme/n)

##Compute the reliability of a service composition
def reliability(P):
    product = 1
    with open(P.Ordering_file, 'rt') as f2:
        reader = csv.reader(f2) 
        for row in reader:
            if not row[0]=='id':
                for service in Service_lake:
                    if str(row[0])==str(service.ide):
                        res = 1
                        for k in range(int(float(row[5]))+1):
                            res=res*service.reliability
                        product = product * res
        return product         


##Compute the availability of a service composition
def availability(P):
    product = 1
    with open(P, 'rt') as f2:
        reader = csv.reader(f2) 
        for row in reader:
            if not row[0]=='id':
                for service in Service_lake:
                   # print("ddddd")
                    if str(row[0])==str(service.ide):
                        res = 1
                        for k in range(int(float(row[5]))+1):
                            res=res*service.availibility
                        product = product * res
        return product 


for f in glob.glob('Plans/*.csv'): # find all csv files
    #print(f)
    os.remove(f)# if file name starts with ExecutableOredering, delete it

timef=0.
Plans=[]

##Create a csv file to represent query plans
entetes = [
     u'id',
     u'name',
     u'duration',
     u'predecessors',
     u'critical',
     u'calls_number'
]
project=[]
Plans=[]

c=1
     


###########################################Specification of services views###################################################
RelevantViews={}
Mappings={}
Queries={}
combinations=Queue.Queue()
Queries["Q1"]=[Recording('a'),Title(a,'t'),PUID(a,'p')]
#Queries["Q(t, p, a, lc)"]=[Book('ob'), BookPublisher(ob, "p"), Author("oa"),AuthorName(oa, "a"), Publisher("op"), Location(op, "lc"), PublisherName(op, "p"),Wrote(oa, ob), Publication(op, ob)]
#Queries["Q1"]=[Book('ob'), Title(ob,"t"), BookAuthor(ob, "a"), BookPublisher(ob, "p"), Author("oa"),AuthorName(oa, "a"), Publisher("op"), Location(op, "lc"), PublisherName(op, "p"),Wrote(oa, ob), Publication(op, ob)]
#print(Book(ob).__class)
services_views = {}
for service in Service_lake:
    services_views[service]=(service.view).view
#############################################I. Selection and Composition of the Relevant Service Views#########################################
#####################################################Specification of Mappings#########################################################
for service_view in services_views.keys():
    Mappings[service_view]=set()
#1. Identify Relevant Service Views
conjuncts=Queue.Queue()
start_time_prog = time.clock()
for conjunct in Queries["Q1"]:
    conjuncts.put(conjunct)
def knap(Cost):
    threads=[]
    thr=multiprocessing.cpu_count()

    for i in range(thr):
        t = threading.Thread(target=worker0, args=())
        t.start()
        threads.append(t)
    conjuncts.join()
    for i in range(thr):
        conjuncts.put(None)
    for t in threads:
        t.join()
    Mappingss=[]
    for Rview in Mappings:
        vi=(Rview.view).name
        si=re.search(r".*?(?=\()", vi)
        Mappingss.append(si)
    # Creation of all possible combinations between different buckets
    #1.Construct a list of different constructed buckets Bi
    Buckets=[]
    nn=0
    for bucket in RelevantViews.values():
        c=list(bucket)
        c.sort(key=int)
        if not c in Buckets:
            Buckets.append(c)
            nn+=len(c)
    comb=myproduct(*Buckets)
    for el in comb:
        combinations.put(el)
    co=1
    Res={'author', 'language', 'publisher'}
    BindAvail0={'isbn'}
    threads = []
    start_time_2 = time.clock()
    for i in range(4):
        t = threading.Thread(target=worker, args=(Res,BindAvail0,))
        t.start()
        threads.append(t)
    combinations.join()
    for i in range(4):
        combinations.put(None)
    for t in threads:
        t.join()
    W=[1]
    # 1: if positive criteria, otherwise 0
    C=[1]
    if len(Plans) >1:
        n=len(Plans)-1
        Q=np.full((n+1, 1), 0.)
        for i in range(0,n+1):
            Q[i,0]=Plans[i].reputation
        wt=[] ###weight/cost of each plan
        i=1
        for plan in Plans:
            wt.append(100*plan.cost)
            i+=1
        Quality=quality_score(Q,W,C)
        val=[]
        for el in Quality:
            a=el
            val.append(a*100)
        ####value to maximize =quality score 
        W = Cost ###maximal cost(threshold to not be exceeded)
        a,b,s=knapSack(W*100, wt, val, n+1)
    else:
        print(str(Plans[0])+"is the only possible plan that can be executed costing "+str(Plans[0].cost)+" dollars, returning results in "+str(Plans[0].response_time)+" seconds, with a reputation equals to "+str(Plans[0].reputation)+", "+str(Plans[0].availibility)+" of availibility"+" , and "+str(Plans[0].reliability)+" of reliability.")
    print("---Total Response Time --- %s seconds ---" % (time.clock() - start_time_prog))
    return a,b,s,Plans

#knap(200,Queries)