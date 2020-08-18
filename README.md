# k-nearest-neighbors implementation
## Implementation of a Knn algorithm on the dataset HC_Body_Temperature

<h4>Ariel University</h4>
<h5>Machine Learning</h5>
<h5>Homework: k-nearest-neighbors</h5>



<h6>1. Implement k-nearest neighbor on the HC Temperature data set:</h6>
 
 ```python
a. Sample 65 training points from the set. 
     The remaining points are the testset.
b. For each of k=1,3,5,7,9 and p=1,2,∞, evaluate the k-NN classifier on the test set, under the lp distance.
  #(The base set of the classifier is the training set.)
     Compute the classifier error on the test set.
c. Repeat steps (a) and (b) 500 times, and print the average error for each k and p. 

```
  <p>
 Which parameters of k,p are the best? Do you see overfitting?
 </p>


<p>
 <h6>2. Prove that the JL-transform preserves dot products up to an additive error of ±ɛ:</h6>
 
 For a set S of normalized vectors, the JL-transform f into O((1/ɛ²)log(|S|)) dimensions ensures that:<br>
 
 (1-ɛ) ǁvǁ ≤ ǁf(v)ǁ ≤ (1+ɛ) ǁvǁ         for all <b>v</b> in <b>S</b> <br>
 and <br>
 (1-ɛ) ǁv-wǁ ≤ ǁf(v-w)ǁ ≤ (1+ɛ) ǁv-wǁ   for all <b>v</b>,<b>w</b> in <b>S</b>. <br>
 Now prove that for some constant c:<br>
 v·w - cɛ ≤ f(v)·f(w) ≤ v·w + cɛ        for all <b>v</b>,<b>w</b> in <b>S</b>. <br>
 
 Hints: Since the JL-transform is linear, ǁf(v-w)ǁ = ǁf(v)-f(w)ǁ.<br>
 Also,  ǁv-wǁ² = ǁvǁ² – 2v·w + ǁwǁ² .
 
 
 </p>
 
 ---
 
 
 

<p>
 <br>
 <h6> Solution:</h6>
The implementation of the algorithm can be found in the codes above.
The code is based on the code from the GeeksforGeeks website:<br>
https://www.geeksforgeeks.org/k-nearest-neighbours/ .<br>
And from what is learned in class
</p>
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

2: 
```

solution:
We saw the following sentences:
   ||u-v||(1-ε)≤||f(u)-f(v)||≤||u-v||(1+ε)
   ||u-v||²(1-ε)≤||f(u)-f(v)||²≤||u-v||²(1+ε)
Also given:
   ||u-v||²=||v||²-2vu+||u||²
Because the normalized vectors exist 1 = ||u||, ||v||
That is:
   ||u-v||²=2-2vu
For each vector v add the vector product of minus 1 (i.e. add -||v||)
So it turns out that:
   ||u-(-v)||=||u+v||
Therefore:
   ||u+v||²(1-ε)≤||f(u)+f(v)||²≤||u+v||²(1+ε),
   ||u+v||²= 2+2uv
Note that:
   ||f(u)+f(v)||²-||f(u)-f(v)||²≤||u+v||²(1+ε) -||u-v||²(1-ε)  
   ||u+v||²(1-ε) -||u-v||²(1+ε)≤||f(u)+f(v)||²-||f(u)-f(v)||²
And also:
   ||f(u)+f(v)||² - ||f(u)-f(v)||²= 4f(u)f(v)
   ||u+v||²(1-ε) -||u-v||²(1+ε)=4vu-4ε
   ||u+v||²(1+ε) -||u-v||²(1-ε)=4uv+4ε
   
We will summarize them together and get:
4vu-4ε ≤4f(v)f(v)≤ 4uv+4ε  → vu-ε≤f(v)f(v)≤uv+ε

```
