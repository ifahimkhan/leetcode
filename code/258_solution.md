
## will it converge ?
$$x, f(x), f(f(x)), ..., f^k(x)$$ 
$$x = \Sigma_{i=0}^{n-1}(d_i\times 10^i)$$
$$f(x) = \Sigma_{i=0}^{n-1}d_i$$
We can see that 
$$f(x) <= x$$

## How fast will it converge
$$x = \Sigma_{i=0}^{n-1}(d_i\times 10^i)$$ 
$$ n \approx log_{10}^x$$
$$f(x) = \Sigma_{i=0}^{n-1}d_i < \Sigma_{i=0}^{n-1}10 = 10n$$
$$ x -> 10 \times log_{10}^x -> ...$$ 
So the run time will be `O(logX)`

## Why `x mod 9` works
We know the base case holds:
$$x \bmod 9 = x \qquad for \qquad x < 9$$
We want to show that:
$$x \bmod 9 = f(x) \bmod 9 $$
Plug in the formula for x and f(x) that is to show:
$$(\Sigma_{i=0}^{n-1}(d_i\times 10^i)) \bmod 9 = (\Sigma_{i=0}^{n-1}d_i) \bmod 9$$
Using the property of modulo:
$$(\Sigma_{i=0}^{n-1}(d_i\times 10^i \bmod 9)) \bmod 9 = (\Sigma_{i=0}^{n-1}(d_i\bmod 9)) \bmod 9$$
We know that
$$d \times (10^i) \bmod 9 = d\times (9999....999 + 1) \bmod 9$$ 
$$ = d \times 99999...999 \bmod 9 + d \times 1 \bmod 9$$
$$ = d \bmod 9 $$
So the left hand side is equal to right hand side
$$(\Sigma_{i=0}^{n-1}(d_i\times 10^i \bmod 9)) \bmod 9 = (\Sigma_{i=0}^{n-1}(d_i\bmod 9)) \bmod 9$$