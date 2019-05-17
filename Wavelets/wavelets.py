import numpy as np
import pywt as pw

def full_compress_wavelets(data, iterations=4):
    std = np.std(data, axis=(0, 1))
    order = []
    itdata = data
    for it in range(iterations):
        ll , (lh, hl, hh) = pw.dwt2(itdata, 'db1')
        itdata = ll
        order += [hh, hl ,lh]
        if it == iterations - 1:
            #print(ll, lh, hl, hh)
            order.append(ll)

    for m in order:
        rows = len(m)
        cols = len(m[0])
        for r in range(rows):
            for c in range(cols):
                if abs(m[r][c]) < std:
                    m[r][c] = 0

    itll = order.pop()
    for it in range(iterations):
        itlh = order.pop()
        ithl = order.pop()
        ithh = order.pop()
        itll = pw.idwt2((itll,(itlh, ithl, ithh)), 'db1')
    return itll 

def multi_compress(data, iterations=3):
    stds = []
    for image in data:
        stds.append(np.std(image, axis=(0, 1)))
    order = []
    itdata = data
    for it in range(iterations):
        r = pw.dwtn(itdata, 'db1')
        aaa = r['aaa']
        aad = r['aad']
        ada = r['ada']
        add = r['add']
        daa = r['daa']
        dad = r['dad']
        dda = r['dda']
        ddd = r['ddd']

        itdata = aaa
        order += [ddd, dda, dad, daa, add, ada, aad]
        if it == iterations - 1:
            order.append(aaa)

    for block in order:
        for m, std in zip(block, stds):
            rows = len(m)
            cols = len(m[0])
            for r in range(rows):
                for c in range(cols):
                    if abs(m[r][c]) < std:
                        m[r][c] = 0

    itll = order.pop()
    for it in range(iterations):
        aad = order.pop()
        ada = order.pop()
        add = order.pop()
        daa = order.pop()
        dad = order.pop()
        dda = order.pop()
        ddd = order.pop() 
        r = {
            'aaa': itll,
            'aad': aad,
            'ada': ada,
            'add': add,
            'daa': daa,
            'dad': dad,
            'dda': dda,
            'ddd': ddd,
        }
        itll = pw.idwtn(r, 'db1')
    return itll

def hjoin(m1, m2):
    joined = []
    for row1, row2 in zip(m1, m2):
        row1 = list(row1)
        row2 = list(row2)
        joined.append(row1 + row2)
    return joined

def vjoined(m1, m2):
    m1 = [ list(row) for row in m1 ]
    m2 = [ list(row) for row in m2 ]
    return m1 + m2

def build(data, iterations=3):
    order = []
    itdata = data
    for it in range(iterations):
        ll , (lh, hl, hh) = pw.dwt2(itdata, 'db1')
        itdata = ll
        order += [hh, hl ,lh]
        if it == iterations - 1:
            order.append(ll)
    
    corder = list(order)
    result = order.pop()
    while order:
        lh = order.pop()
        hl = order.pop()
        hh = order.pop()
        result = vjoined(hjoin(result, hl), hjoin(lh, hh))
    
    return np.asarray(result), corder

def calc(m1, m2):
    m1 = [ list(row) for row in m1 ]
    m2 = [ list(row) for row in m2 ]
    s = 0
    for r1, r2 in zip(m1, m2):
        for c1, c2 in zip(r1, r2):
            s += abs(c1 - c2)
            #print(s)
    return s


def unbuild(data):
    udata = []
    for order in [ d[1] for d in data ]:
        itll = order.pop()
        while order:
            itlh = order.pop()
            ithl = order.pop()
            ithh = order.pop()
            itll = pw.idwt2((itll,(itlh, ithl, ithh)), 'db1')
        udata.append(itll)
    return udata


def time_compression(data, tolerance, iterations=3):
    tdata = [ build(frame, iterations=iterations) for frame in data ]
    cdata = []
    while tdata:
        rep = tdata[0]
        cdata.append(rep)
        tdata = tdata[1:]
        temp = []
        for it, frame in enumerate(tdata):
            d = calc(rep[0], frame[0])
            if d > tolerance:
                print(d)
                temp = tdata[it:]
                break
        tdata = temp
    cdata = unbuild(cdata)
    return cdata
