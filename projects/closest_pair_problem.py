import math
import random
import numpy

def euclid(pt0, pt1):
    return math.sqrt(sum(map(lambda x, y: (x - y) ** 2, pt0, pt1)))

def one_norm(pt0, pt1):
    return sum(map(lambda x, y: abs(x - y), pt0, pt1))

def inf_norm(pt0, pt1):
    return max(map(lambda x, y: abs(x - y), pt0, pt1))

def distance(pt0, pt1):
    return inf_norm(pt0, pt1)

def brute_force(ptlst):
    min_dist = distance(ptlst[0], ptlst[1])
    pair = (ptlst[0], ptlst[1])
    for i in range(len(ptlst)):
        for j in range(i+1,len(ptlst)):
            dist = distance(ptlst[i], ptlst[j])
            if dist < min_dist:
                min_dist = dist
                pair = (ptlst[i], ptlst[j])
    return min_dist, pair

def median_divide(xsort, ysort):
    l = len(xsort)
    median = xsort[l/2][0]
    leftx = xsort[:l/2]
    rightx = xsort[l/2:]
    lefty = []
    righty = []
    for i in ysort:
        if i[0] < median:
            lefty.append(i)
        else:
            righty.append(i)
    return median, leftx, lefty, rightx, righty

def divide_conquer(xsort, ysort):
    if len(xsort) <= 3:
        return brute_force(xsort)
    median, leftx, lefty, rightx, righty = median_divide(xsort, ysort)
    min0, pair0 = divide_conquer(leftx, lefty)
    min1, pair1 = divide_conquer(rightx, righty)
    (m, pair) = (min0, pair0) if min0 < min1 else (min1, pair1)
    leftj, rightj = median - m, median + m
    yy = []
    for pt in ysort:
        if leftj < pt[0] < rightj:
            yy.append(pt)
    l = len(yy)
    for i in range(l):
        for j in range(i+1,min(l,i+8)):
            dist = distance(yy[i], yy[j])
            if dist < m:
                m, pair = dist, (yy[i], yy[j])
    return m, pair

def closest_pair(ptlst):
    from copy import deepcopy
    xsort = deepcopy(ptlst)
    xsort = sorted(xsort, key=lambda pt: pt[0])
    ysort = deepcopy(ptlst)
    ysort = sorted(ysort, key=lambda pt: pt[1])
    return divide_conquer(xsort, ysort)

def gen_random_matrix(m, n):
    return [[random.random() for j in range(n)] for i in range(m)]

if __name__ == "__main__":
    ptlst = gen_random_matrix(60, 3)
    ret0 = closest_pair(ptlst)
    ret1 = brute_force(ptlst)
    if ret0[0] > ret1[0]:
        print "wrong"
    else:
        print "right"
