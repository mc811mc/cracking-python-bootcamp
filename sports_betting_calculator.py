print("Welcome to the odds calculator")
odds = int(input("Enter the odds: "))
wager = int(input("Enter wager (bet amount): "))
print("Bet", wager)

if odds > 0:
    win = wager / 100 * odds
    probability = 100 / (odds + 100) * 100
elif odds < 0:
    win = wager / abs(odds) * 100
    probability = abs(odds) / (abs(odds) + 100) * 100

print("To Win", abs(win))
payout = abs(wager) + abs(win)
print("Payout", payout)
print("American Odds:", odds)
print("Fractional Odds", abs(win/wager))
print("Decimal Odds:", abs(payout/wager))
print("Implied Probability:", probability)



