"""
309: Best Time to Buy and Sell Stock with Cooldown

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 
Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""


def maximum_profits(prices: list[int]) -> int:
    """
    Compute maximum profits.

    Start at the first day and compute profits, greedily taking the best (legal)
    option from the previous day. We can track 4 options, BUY, SELL, HOLD, and
    WAIT.
    """
    MIN_INT = -5000 * 1000  # lower bound on profit based on constraints

    BUY = 0
    SELL = 1
    HOLD = 2
    WAIT = 3

    profits = [
        -prices.pop(0),  # profit on the first day if BUY is -price
        MIN_INT,  # can't sell on the first day
        MIN_INT,  # can't hold on the first day
        0,  # if waiting, profit is zero on the first day
    ]

    for price in prices:
        profits = [
            profits[WAIT] - price,
            max(profits[HOLD], profits[BUY]) + price,
            max(profits[BUY], profits[HOLD]),
            max(profits[SELL], profits[WAIT]),
        ]
    return max(*profits)
