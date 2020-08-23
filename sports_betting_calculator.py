print("Welcome to the odds calculator")
odds = int(input("Enter the odds: "))
wager = int(input("Enter wager (bet amount): "))
print("Bet", wager, "\n")

if odds > 0:
    win = wager / 100 * odds
    probability = 100 / (odds + 100) * 100
elif odds < 0:
    win = wager / abs(odds) * 100
    probability = abs(odds) / (abs(odds) + 100) * 100

#variable
payout = abs(wager) + abs(win)
fractional_odds = abs(win/wager)
decimal_odds = abs(payout/wager)

print("Statistics List \n")
print("To Win:", abs(win))
print("Payout:", payout)
print("American Odds:", odds)
print("Fractional Odds", fractional_odds)
print("Decimal Odds:", decimal_odds)
print("Implied Probability:", probability)



