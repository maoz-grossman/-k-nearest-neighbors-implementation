#!/usr/bin/env python
# coding: utf-8

#import numpy as np
import random 
import time 




class point:
    def __init__(self , x=0,gender=1,y=0):
        self.x=float(x)
        self.y= float(y)
        self.gender=int(gender)
        self.weight=0



def K_nn(Base, k, p , point):
    distances=[]
    male=0
    female=0
    for base in Base:
        dist= L_p(p,base,point)
        distances.append((dist,base.gender))
    distances.sort(key = lambda x: x[0])
    k_dist=distances[:k] #Takes the k first elements from the sorted list
    for d in k_dist:
        if d[1]==1:
            male+=1
        if d[1]==-1:
            female+=1
    if female>male:
        return -1
    return 1
        




def L_p(p,point1,point2):
    if p==float('inf'):
        return max(abs(point1.x-point2.x),abs(point1.y-point2.y))
    return ((abs(point1.x-point2.x))**p+(abs(point1.y-point2.y))**p)**(1/p)



def get_data_of_HC_Body_Temperature():
    file_name='HC_Body_Temperature'
    f= open(file_name, "r")
    data_set=[]
    for line in f:
        txt = line
        str_points= txt.split()
        #print(str_points)
        if str_points[1] != str(1):
            x= point(str_points[0],-1,str_points[2])
        else:
            x= point(str_points[0],str_points[1],str_points[2])
        data_set.append(x)  
    return data_set



Data_set =get_data_of_HC_Body_Temperature()
p_s=[1,2,float('inf')]
tic = time.perf_counter()
best_result=[0,0,1]
rounds=500
for k in range(1,10,2):
    print("~~~~~ k=",k,"~~~~~")
    for p in p_s:
        error_test=0
        error_train=0
        for i in range(rounds):
            random.shuffle(Data_set)
            base=Data_set[0:65]
            test=Data_set[66:]
            for x in test:
                guess=K_nn(base,k,p,x)
                if guess!= x.gender:
                    error_test+=1
            for x in base:
                guess=K_nn(base,k,p,x)
                if guess!= x.gender:
                    error_train+=1
        error_train= error_train/rounds/65
        error_test=error_test/rounds/65
        #Find the best result of k and p in test
        if error_test<best_result[2]:
            best_result[0]=k
            best_result[1]=p
            best_result[2]=error_test
        print("p=",p," The average percentage error in training:","%.3f" % error_train,"% (","%.3f" % (1-error_train),"% were correct)")
        print("p=",p," The average percentage error in test:","%.3f" % error_test,"% (","%.3f" % (1-error_test),"% were correct)")


print("\nBest result for k=",best_result[0]," and p=",best_result[1]," with average error of ",best_result[2])       
toc=time.perf_counter()
print("\nthe program took", "%.4f"%((toc - tic)/60), "minutes")



