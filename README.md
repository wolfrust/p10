# P10 

This program looks at the number of primes found between powers of 10.

----

### Files

`p10.py` - run this
```
for i in range(9, 12): # modify this line if you want to change the powers of 10 between which it searches
    primes = []
    for x in range(pow(10, i-1), pow(10, i)):
        if is_prime(x):
            primes.append(x)
    print(f'{pow(10, i-1)}-{pow(10, i)}', len(primes), len(primes)/(pow(10, i) - pow(10, i-1)))
```

Three things to note here:
- if you use range(1, 10), it will show ratios from 1-10, 10-100, 100-1000,...., 10^9-10^10 seperately
- if you enter range(5, 7), it will start from 10^4-10^5, not 10^5-10^6
- [this is the method used to test primality](https://en.wikipedia.org/wiki/Primality_test#:~:text=We%20can%20improve%20this%20method%20further.) — it uses the 6k+-1 optimization

---
`p10plot.py` - plot graphs of values
you *will* need to edit this and run it as per your liking

---
`*.png` - two graphs of my results
