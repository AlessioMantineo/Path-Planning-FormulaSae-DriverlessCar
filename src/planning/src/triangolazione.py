#!/usr/bin/env python3
import rospy
from planning.msg import point
from planning.msg import point_array
from planning.msg import coni_posizione
from turtlesim.msg import Pose
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np
from array import array
import copy


def distanza(x1,y1,x2,y2):
    import math
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
def puntomediox(xa,xb):
    x=((xa+xb)/2)
    return x
def puntomedioy(ya,yb):
    y=((ya+yb)/2)
    return y

def crea_punti(xa,xb,ya,yb,coni):
   
    coni_mezzo=np.array([]) #punti di mezzo
    for i in xa:
        x=puntomediox(xa[i],xb[i])
        y=puntomedioy(ya[i],yb[i])      
        coni_mezzo[i]=([x,y])
        print(coni_mezzo[i])
        
    return coni_mezzo
#funzione per la creazione dei punti di mezzo tra i coni        
def crea_punti(destra,sinistra,copia):
    k=1
    i=0
    prova=destra
    lista=[]
    for (xd,yd) in destra:
        xs,ys=sinistra[i]
        i=i+1
        x=puntomediox(xd,xs)
        y=puntomedioy(yd,ys)
        copia=aggiungi(copia,x,y)
        if k<len(destra):
             futuroxd,futuroyd=destra[k]
             k=k+1
             xavanti=puntomediox(xs,futuroxd)
             yavanti=puntomedioy(ys,futuroyd) 
             copia=aggiungi(copia,xavanti,yavanti)
    return copia   
"""
def punti_delaunay(triangoli,copia):
    i=0
    g=0
    k=1
    z=2
    n=len(triangoli)
    print(n)
    for r in range(n):
        
        if i in(0,2): #secondo con tutti
            #ho matrice con [v1 v2 v3] per accedere uso 000 011 02, esempio print(triangoli[3][1][0])
            primopuntox=puntomediox((triangoli[i][k][0]),(triangoli[i][0][0]))
            primopuntoy=puntomedioy((triangoli[i][k][k]),(triangoli[i][0][k]))
            secondopuntox=puntomediox((triangoli[i][k][0]),(triangoli[i][z][0]))
            secondopuntoy=puntomedioy((triangoli[i][k][k]),(triangoli[i][z][k]))    
            #stampa(primopuntox,primopuntoy,secondopuntox,secondopuntoy)
            #copia=np.append(copia,np.array([[primopuntox,primopuntoy]]),axis=0)
            copia=aggiungi(copia,primopuntox,primopuntoy)
            copia=aggiungi(copia,secondopuntox,secondopuntoy)
        """"
"""
        if ((i%2)==0) and i!=(0,2): #il primo con tutti
            primopuntox=puntomediox((triangoli[i][0][0]),(triangoli[i][k][0]))
            primopuntoy=puntomedioy((triangoli[i][0][k]),(triangoli[i][k][k]))
            secondopuntox=puntomediox((triangoli[i][0][0]),(triangoli[i][z][0]))
            secondopuntoy=puntomedioy((triangoli[i][0][k]),(triangoli[i][z][k])) 
            stampa(primopuntox,primopuntoy,secondopuntox,secondopuntoy)
            """
"""   
        if((i%2)!=0 and i!=1):   
            #terzo con tutti
            primopuntox=puntomediox((triangoli[i][z][0]),(triangoli[i][0][0]))
            primopuntoy=puntomedioy((triangoli[i][z][k]),(triangoli[i][0][k]))
            secondopuntox=puntomediox((triangoli[i][z][0]),(triangoli[i][k][0]))
            secondopuntoy=puntomedioy((triangoli[i][z][k]),(triangoli[i][k][k]))
            copia=aggiungi(copia,primopuntox,primopuntoy)
            copia=aggiungi(copia,secondopuntox,secondopuntoy)
            #stampa(primopuntox,primopuntoy,secondopuntox,secondopuntoy)
        i=i+1
    return copia       
"""
def aggiungi(copia,x,y):
    copia=np.append(copia,np.array([[x,y]]),axis=0)
    return copia

def stampa(a,b,c,d):
    plt.plot(a,b,color='red',marker='o')
    #plt.plot(c,d,color="blue",marker="o")
    return

def converti_lista(percorso):
    convertito = point_array()
    for p in percorso:
        elem = point()
        elem.x = p[0]
        elem.y = p[1]
        convertito.cones.insert(0, elem)
        plt.plot(elem.x,elem.y,color='red',marker='o')
    return convertito 

def main():
    print("Start " + __file__)
    rospy.init_node('planning', anonymous=True)
    #track = point_array()
    pose = Pose()
    path_pub = rospy.Publisher('path', point_array, queue_size=10)
    print("In attesa di un messaggio")
    pose = rospy.wait_for_message("/turtle1/pose", Pose, timeout=None)
 
    
    #coni che arrivano dalla parte di visione
    points = np.array([[4,6.5],[3,6.5],[2,6.5],[4,3.5],[3,3.5],[2,3.5]])
    #coni vengono divisi in coni di destra e sinistra
    coni_sinistra=np.array([[4,6.5],[3,6.5],[2,6.5]])
    coni_destra=np.array([[4,3.5],[3,3.5],[2,3.5]])

    tri = Delaunay(points)

    plt.triplot(points[:,0], points[:,1], tri.simplices)
    plt.plot(points[:,0], points[:,1], '^')

    coni=4 #coni per lato
    triangoli=(points[tri.simplices])
    """
    #print(triangoli)
    #print(triangoli[3][1][0])
    """
    copia=np.empty((0,2),float)
    """
    #copia=punti_delaunay(triangoli,copia)
    #copia=np.append(copia,np.array([[2,3.5]]),axis=0)
    """
    copia=crea_punti(coni_destra,coni_sinistra,copia)
    plt.plot(copia[:,0],copia[:,1],'o')
    """
    #print(copia)
    """
    percorso_convertito = point_array()
    print("found path!!")
    print("PERCORSO CONVERTITO")
    percorso_convertito = converti_lista(copia)
    for z in percorso_convertito.cones:
        print(z.x, z.y)
    path_pub.publish(percorso_convertito)
    """
    print (copia)
    print("_____________________")
    print(percorso_convertito)
    plt.plot(percorso_convertito)
    """
    plt.show()
    
if __name__=='__main__':
    main()