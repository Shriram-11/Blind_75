
def maxProfit(prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""

	#assume we buy a stack on day one, so purchase is prices[0] and there is no profit
	purchase,profit=prices[0],0

	#traverse list from index 1
	for p in prices[1:]:
			#if we are getting a profit by selling a stock, update profit to store maximum possible profit
			profit=max(profit,p-purchase)
			#if current price is less than purchase prices price chage purchase
			purchase=min(purchase,p)
	return profit 
