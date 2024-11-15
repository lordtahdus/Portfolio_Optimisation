*(This is an extension from university assignment)*

A simple Portfolio Optimisation problem: Mean-variance method with additional constraints

## Description:

We download the historical data from Yahoo finance for 18 stocks, in 3 years, and compute the daily log return (using the close price). 

Given the 729 different portfolios we choose, we will optimise each one. The objective function to optimise is the return per risk, or, $$\frac{𝑚𝑒𝑎𝑛.𝑜𝑓.𝑙𝑜𝑔.𝑟𝑒𝑡𝑢𝑟𝑛𝑠}{𝑣𝑎𝑟𝑖𝑎𝑛𝑐𝑒.𝑜𝑓.𝑙𝑜𝑔.𝑟𝑒𝑡𝑢𝑟𝑛𝑠}$$ 
 
Denote mean of log returns for stock i by $$\bar{𝑟_𝑖}$$ and its weight by $$𝑤_𝑖$$, we get: 

- Mean of Portfolio Returns: $$\bar{𝑟_P} = 𝑤'\bar{𝑟}$$, where 𝒓̅ and 𝒘 are column vectors
- Variance of portfolio returns: $$Var(\bar{𝑟_P}) = 𝑤'Var(\bar{𝑟})w$$

<br>

**Optimisation function:**

$$\underset{w}{\mathrm{max}} ( \{𝑤'\bar{𝑟}[𝑤'Var(\bar{𝑟})w]^{-1}\} )$$

- subject to:

$$w\mathbf{1} = 1$$

<p align="center"> $$w_i \in [0.1, 1]$$, for i = 1,2,...,6 </p>

<br>

We choose this objective function because we want to maximise the return and account for the risks, instead of solely miminising the standard deviation, which would trade off the return. We also set a lower bound for the weight for each stock, to prevent cases in which some stocks get 0 allocation. This would ensure that we have a good profit and diversify at the same time.

<br>

<p align="center">
  <span style="display: inline-block; border: 1px solid #ccc; border-radius: 8px;">
    <img src="ETC3460\fig_729_opt_port.png" alt="Pearls" width="700">
    <br>
    Figure 1
  </span>
</p>
