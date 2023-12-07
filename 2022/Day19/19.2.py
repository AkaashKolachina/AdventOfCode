from sys import argv
from collections import defaultdict
from math import ceil

data = open(argv[1]).read()
lines = [line for line in data.split('\n')]

blueprints = []
for line in lines[:3]:
    prices = [int(x) for x in line.split() if x.isdigit()]
    price_tup = (prices[0], prices[1], (prices[2], prices[3]), (prices[4], prices[5]))
    blueprints.append(price_tup)

def dfs(prices):
    T = [ ( t - 1 ) * t // 2 for t in range( 32 + 1 ) ]
    (ore_bot_price, clay_bot_price, obs_bot_price, geode_bot_price) = prices
    max_ore = max([ore_bot_price, clay_bot_price, obs_bot_price[0], geode_bot_price[0]])
    max_clay = obs_bot_price[1]
    max_obs = geode_bot_price[1]
    visited = set()
    s = []
    max_geodes = 0
    cache = defaultdict(int)
    #(time, ore, clay, obsidian, geode, ore_bot, clay_bot, obs_bot, geode_bot)
    start = (32,0,0,0,0,1,0,0,0)
    s.append(start)

    while len(s) > 0:
        step = s.pop()
        (time, ore, clay, obsidian, geode, ore_bot, clay_bot, obs_bot, geode_bot) = step
        if step in visited:
            continue
        visited.add(step)
        if time < 0:
            continue
        if cache[(ore, clay, obsidian, geode, ore_bot, clay_bot, obs_bot, geode_bot)] > time:
            continue
        cache[(ore, clay, obsidian, geode, ore_bot, clay_bot, obs_bot, geode_bot)] = time
        max_geodes = max(max_geodes, geode)

        if (geode + (geode_bot * time) + T[time]) <= max_geodes:
            continue

        if time == 1:
            next = (time - 1, ore + ore_bot, clay + clay_bot, obsidian + obs_bot, geode + geode_bot, ore_bot + 1, clay_bot, obs_bot, geode_bot)
            s.append(next)
            continue

        if ore_bot <= max_ore:
            if ore >= ore_bot_price:
                next = (time - 1, ore - ore_bot_price + ore_bot, clay + clay_bot, obsidian + obs_bot, geode + geode_bot, ore_bot + 1, clay_bot, obs_bot, geode_bot)
                s.append(next)
            else:
                dt = int(ceil((ore_bot_price - (ore)) / ore_bot))
                next = (time - dt - 1, ore + (ore_bot * (dt + 1)) - ore_bot_price, clay + (clay_bot * (dt + 1)) , obsidian + (obs_bot * (dt + 1)), geode + (geode_bot * (dt + 1)), ore_bot + 1, clay_bot, obs_bot, geode_bot)
                s.append(next)

        if clay_bot <= max_clay:
            if ore >= clay_bot_price:
                next = (time - 1, ore - clay_bot_price + ore_bot, clay + clay_bot, obsidian + obs_bot, geode + geode_bot, ore_bot, clay_bot + 1, obs_bot, geode_bot)
                s.append(next)
            else:
                dt = int(ceil((clay_bot_price - (ore)) / ore_bot))
                next = (time - dt - 1, ore + (ore_bot * (dt + 1)) - clay_bot_price, clay + (clay_bot * (dt + 1)), obsidian + (obs_bot * (dt + 1)), geode + (geode_bot * (dt + 1)), ore_bot, clay_bot + 1, obs_bot, geode_bot)
                s.append(next)
        
        if obs_bot <= max_obs:
            if ore >= obs_bot_price[0] and clay >= obs_bot_price[1]:
                next = (time - 1, ore - obs_bot_price[0] + ore_bot, clay - obs_bot_price[1] + clay_bot, obsidian + obs_bot, geode + geode_bot, ore_bot, clay_bot, obs_bot + 1, geode_bot)
                s.append(next)
            elif clay_bot > 0:
                dt = max((ceil((obs_bot_price[0]  - (ore)) / ore_bot)), int(ceil((obs_bot_price[1]  - (clay)) / clay_bot)))
                next = (time - dt - 1, ore + (ore_bot * (dt + 1)) - obs_bot_price[0], clay + (clay_bot * (dt + 1)) - obs_bot_price[1], obsidian + (obs_bot * (dt + 1)), geode + (geode_bot * (dt + 1)), ore_bot, clay_bot, obs_bot + 1, geode_bot)
                s.append(next)

        if ore >= geode_bot_price[0] and obsidian >= geode_bot_price[1]:
            next = (time - 1, ore - geode_bot_price[0] + ore_bot, clay + clay_bot, obsidian - geode_bot_price[1] + obs_bot, geode + geode_bot, ore_bot, clay_bot, obs_bot, geode_bot + 1)
            s.append(next)
        elif obs_bot > 0:
            dt = max((ceil((geode_bot_price[0]  - (ore)) / ore_bot)), int(ceil((geode_bot_price[1]  - (obsidian)) / obs_bot)))
            next = (time - dt - 1, ore + (ore_bot * (dt + 1)) - geode_bot_price[0], clay + (clay_bot * (dt + 1)), obsidian + (obs_bot * (dt + 1)) - geode_bot_price[1], geode + (geode_bot * (dt + 1)), ore_bot, clay_bot, obs_bot, geode_bot + 1)
            s.append(next)

    return max_geodes

prod = 1
for i,bp in enumerate(blueprints):
    geodes = dfs(bp)
    id = i + 1
    prod *= geodes
    print(id, geodes)
print(prod)