import numpy as np
import re
import decimal


rule_names=[]
rules=[]
### Parsing

r1=re.compile("(.+): (\d+)-(\d+) or (\d+)-(\d+)")
with open('resources/day_16_tickets-data.txt','r') as f:
    while(True): 
        m=r1.match(f.readline().strip())
        if not m:
            break
        rule_names.append(m.groups()[0])
        rules.append(list(map(int, m.groups()[1:])))
    rules=np.array(rules, dtype=int)

    while (True):
        d=f.readline().strip()
        if "your ticket" in d:
            mt = np.array(list(map(int, f.readline().split(","))), dtype=int)
        elif "nearby tickets" in d:
            tickets=np.genfromtxt(f.read().split('\n'), delimiter=',', dtype='int')
            break

#find invalid:

def apply_func(ticket, field, rule):
    r=rules[rule]
    v=tickets[ticket, field]
    return ((r[0]<=v & v<= r[1])|(r[2]<=v & v<= r[3]))

vmatrix=np.fromfunction(np.vectorize(apply_func), (tickets.shape[0], tickets.shape[1], rules.shape[0]), dtype=int)

print("Bad ticket sum",np.sum(tickets[np.where(vmatrix.sum(axis=2)==0)]))
good_tickets=np.delete(tickets, np.where(vmatrix.sum(axis=2)==0)[0], 0)
good_matrix=np.delete(vmatrix, np.where(vmatrix.sum(axis=2)==0)[0], 0)

valid=good_matrix.sum(axis=0)==good_matrix.shape[0]



product=1

#compute the magic square
mask=np.ones(valid.shape, dtype='bool')
for i in range(valid.shape[0]):
    cur=valid & mask
    axissum=cur.sum(axis=1)
    field=np.where(axissum==1)[0][0]
    rule=np.where(cur[field, :]==True)[0][0]
    if rule_names[rule].startswith("departure"):
        #print(field, rule, mt[field])
        product *= int(mt[field])
    mask[:,rule]=False

print ("Product", product)
