*(This is a university assignment)*

A simple Portfolio Optimisation problem: Mean-variance method with additional constraints

## Description:

We download the historical data from Yahoo finance for 18 stocks, in 3 years, and compute the daily log return (using the close price). 

Given the 729 different portfolio we choose, we will optimise each one. The objective function to optimise is the return per risk, in order words, $$𝑚𝑒𝑎𝑛 𝑜𝑓 𝑙𝑜𝑔 𝑟𝑒𝑡𝑢𝑟𝑛𝑠/𝑣𝑎𝑟𝑖𝑎𝑛𝑐𝑒 𝑜𝑓 𝑙𝑜𝑔 𝑟𝑒𝑡𝑢𝑟𝑛𝑠$$ 
 
 Denote mean of log returns for stock i by 𝑟𝑖 and its weight by 𝑤𝑖, we get: 
