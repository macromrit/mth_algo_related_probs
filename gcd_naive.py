"""
pros:
  programmmer friendly i.e easily conceivable 
  no intense math required - this's the pythonic way of solving this
cons:
  Being primitive make this snippets time complexity worse at collasal cases
"""

def naive_gcd(a : int, b : int)->int:
    assert a>=0 and b>=0 and a+b>0
    
    if not a or not b:
        return max(a,b)
    
    for d in range(min(a,b), 0, -1):
        if not a%d and not b%d:
            return d
          
  
