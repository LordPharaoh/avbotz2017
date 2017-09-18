coins = [int(a) for a in open("coins2.in", "r").readline().strip().split(" ")]
val = coins[0]
coins = coins[1:]
results = {}

def recurse(value):
	min_coins = value
	if value in coins:
		results[value] = 1
		return 1	
	try:
		return results[value]
	except KeyError:
		for c in coins:
			if c > value:
				continue
			n = 1 + recurse(value - c)
			if n < min_coins:
				min_coins = n
			results[value] = min_coins
		return min_coins

open("coins2.out","w").write(str(recurse(val)) + "\n")
