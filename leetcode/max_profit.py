class Solution(object):
    def maxProfit(self, prices, fee):
        current_balance = 0
        balance_after_buy = -prices[0]
        transactions = []
        buy_index = 0

        for i in range(1, len(prices)):
            previous_balance = current_balance

            balance_if_sell_today = balance_after_buy + prices[i] - fee
            if balance_if_sell_today > current_balance:
                current_balance = balance_if_sell_today
                # Sell today, if we're not in the middle of a transaction, start one.
                if not transactions or buy_index > transactions[-1][1]:
                    transactions.append((buy_index, i))
                else:  # We're in the middle of a transaction, so update it.
                    transactions[-1] = (transactions[-1][0], i)

            balance_if_buy_today = previous_balance - prices[i]
            if balance_if_buy_today > balance_after_buy or i == len(prices) - 1:
                balance_after_buy = balance_if_buy_today
                buy_index = i  # Buy today, remember the index.

        return current_balance, transactions

prices = [1,5,9]
fee = 2
prices = [7, 1, 5, 3, 6, 4]
fee = 0
print(Solution().maxProfit(prices, fee))