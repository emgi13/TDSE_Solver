# Solving Time-Dependent Schrödinger Equations in Python

## Introduction
Based on [this article](https://medium.com/intuition/solve-the-time-dependent-schr%C3%B6dinger-equation-in-less-than-12-lines-of-python-3663077b1fbd) by Mathcube

Any quantum mechanical system evolves according to the TDSE given below
```math
\frac{\partial}{\partial t} \left| \psi (t) \right> = - i H (t) \left| \psi (t) \right>
```
To simulate this emulation, we need to solve this differential equation. We can use the Euler Approximation (1<sup>st</sup> Order approximation) by discretizing the time domain. The differential equation is then approximated in the forward direction by
```math
\frac{\left| \psi \right>^{(n+1)} - \left| \psi \right>^{(n)}}{\Delta t} = -i H \left| \psi \right>^{(n)} 
``` 
where
```math
\left| \psi \right>^{(n)} = \left| \psi (n \Delta t) \right>
```

This gives us the Explicit form of the wave-function at the next time step.
```math
\left| \psi \right>^{(n+1)} = (1 - i H \Delta t) \left| \psi \right>^{(n)}
```
Similarly for the backward approximation
```math
\frac{\left| \psi \right>^{(n+1)} - \left| \psi \right>^{(n)}}{\Delta t} = -i H \left| \psi \right>^{(n+1)} 
``` 
we get the implicit form
```math
(1 + i H \Delta t) \left| \psi \right>^{(n+1)} =  \left| \psi \right>^{(n)}
```
But in these approximation, we lose the normalization of the wave-function.
![Evolution of Wavepacket](Solution.gif)
