#!/usr/bin/python

import argparse

def find_max_profit(prices):
  
  current_min_price_so_far = min(prices[:-1])
  max_profit_so_far = 0
 
  # second_max_price = (prices[-2] - prices[-1])
  # second_min_price = prices[-2] - prices[1]


  # if len(prices) == 5 and prices.sort() != max_profit_so_far or prices.sort() != second_max_price:
  #   return max_profit_so_far - current_min_price_so_far
  # # elif:
  # #   return second_max_price
  # else:
  #   return second_min_price
      
  
  # return max_profit_so_far - current_min_price_so_far
  for i in range(prices.index(current_min_price_so_far)+1 , len(prices)):
    if prices[i] > max_profit_so_far:
      max_profit_so_far = prices[i]
  return max_profit_so_far - current_min_price_so_far
      

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))