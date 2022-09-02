#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt



# In[2]:


import Odorant_Stim_fourodors


# In[30]:


import csv
import collections

def read_connections(filename):
    #r = list(csv.reader(open('updated_erecta_all_circuitry_absolute.csv'))) #Need to get updated connectivity from Ruairi with all neurons
    #r = list(csv.reader(open('updated_melanogaster_all_circuitry_absolute.csv'))) #does this need to be changed to 'filename'?
    r = list(csv.reader(open(filename)))
        
    header = r[0]
    data = r[1:]

    conns = {}
    for row in data:
        for i, item in enumerate(row):
            if i > 0:
                pre = row[0]
                post = header[i]
                c = int(item)
                if c > 0:
                    if pre not in conns:
                        conns[pre] = {}
                    conns[pre][post] = c
                    
    ORNs_left = [name for name in header if 'ORN' in name and 'left' in name]
    ORNs_right = [name for name in header if 'ORN' in name and 'right' in name]
    uPNs_left = [name for name in header if ' uPN' in name and 'left' in name]
    uPNs_right = [name for name in header if ' uPN' in name and 'right' in name]
    mPNs_left = [name for name in header if 'mPN' in name and 'left' in name]
    mPNs_right = [name for name in header if 'mPN' in name and 'right' in name]
    Pickys_left = [name for name in header if 'icky' in name and 'left' in name]
    Pickys_right = [name for name in header if 'icky' in name and 'right' in name]
    Choosys_left = [name for name in header if 'hoosy' in name and 'left' in name]
    Choosys_right = [name for name in header if 'hoosy' in name and 'right' in name]
    Broads_left = [name for name in header if 'road' in name and 'left' in name]
    Broads_right = [name for name in header if 'road' in name and 'right' in name]
    Keystone_left = [name for name in header if 'eystone' in name and 'left' in name]
    Keystone_right = [name for name in header if 'eystone' in name and 'right' in name]
    Ventral_left = [name for name in header if 'entral' in name and 'left' in name]
    Ventral_right = [name for name in header if 'entral' in name and 'right' in name]

        
    Names = collections.namedtuple('Names', ['ORNs_left', 'uPNs_left', 'mPNs_left', 'Pickys_left',
                                                  'Choosys_left','Broads_left','Keystone_left','Ventral_left',
                                            'ORNs_right', 'uPNs_right', 'mPNs_right', 'Pickys_right',
                                                  'Choosys_right','Broads_right','Keystone_right','Ventral_right'])
    
    
    return conns, Names(ORNs_left, uPNs_left, mPNs_left, Pickys_left,
                             Choosys_left,Broads_left,Keystone_left,Ventral_left,
                             ORNs_right, uPNs_right, mPNs_right, Pickys_right,
                             Choosys_right,Broads_right,Keystone_right,Ventral_right)

def make_weights(conns, pre, post):
    w = np.zeros((len(post), len(pre))) #note: pre/post switched in output array for print(make_weights())
    for i, pre_n in enumerate(pre):
        for j, post_n in enumerate(post):
            if post_n in conns[pre_n]:
                w[j,i] = conns[pre_n][post_n] 
    return w

