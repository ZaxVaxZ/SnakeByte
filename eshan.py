```
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def debug(msg):
    print(msg, file=sys.stderr, flush=True)

def parse_snake(body_str):
    parts = body_str.split(":")
    return [tuple(map(int, pos.split(','))) for pos in parts]

def taxicab(head_pos, pos):
    x1, y1 = head_pos
    x2, y2 = pos
    d = abs(x2 - x1) + abs(y2 - y1)
    return (d)

def find_nearest(head_pos, sources):
    nearest = ()
    min_dist = float("inf")

    for pos in sources:
        dist = taxicab(head_pos, pos)
        if dist < min_dist:
            min_dist = dist
            nearest = pos

# static (stays the same)

my_id = None
width = 0
height = 0
grid = []
my_snakebot_ids = []
opp_snakebot_ids = []

# dynamic (changes with game loop)

power_sources = []
snakebots = {}

debug("STARTING BOT")

my_id = int(input())
width = int(input())
height = int(input())

debug(f"ID: {my_id}, Grid Size: {width}x{height}")

for i in range(height):
    grid.append(input())
    debug(grid[i])

debug(f"Grid loaded: {len(grid)} rows")

snakebots_per_player = int(input())
for i in range(snakebots_per_player):
    my_snakebot_ids.append(int(input()))

for i in range(snakebots_per_player):
     opp_snakebot_ids.append(int(input()))

debug(f"My snakebots: {my_snakebot_ids}")
debug(f"Opponent snakebots: {opp_snakebot_ids}")

turns = 0
while True:
    turns += 1
    power_sources = []
    power_source_count = int(input())
    for i in range(power_source_count):
        coords = input().split()
        x, y = [int(j) for j in coords]
        power_sources.append((x, y))
    debug(f"Power sources: {len(power_sources)}, {power_sources}")

    snakebots = {}
    snakebot_count = int(input())
    for i in range(snakebot_count):
        inputs = input().split()
        snakebot_id = int(inputs[0])
        body_string = inputs[1]
        
        body = parse_snake(body_string)
        if body:
            head = body[0]
            owner = "me" if snakebot_id in my_snakebot_ids else "opp"
            snakebots[snakebot_id] = {
                "owner": owner,
                "body": body,
                "head": head,
                "size": len(body),
            }
    debug(f"Active snakebots: {snakebot_count}")

    # every body part should also be a wall, so collecting everything
    all_body_parts = set()
    for bot_id, bot_data in snakebots.items():
        for part in bot_data["body"]:
            all_body_parts.add(part)
    debug(f"{all_body_parts}")
    break
```