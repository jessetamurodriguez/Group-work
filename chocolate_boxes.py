# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yulian Villarreal
# Jese Rodriguez
# Amber Perez
# Jose Godoy
# Section: M02
# Assignment: Lab Topic 10 (team)
# Date: 28/10/2026
import random
import time


NOISE = 0.1          # chance of taking a random swap instead of the best one
SAMPLE = 40          # max number of other boxes checked for swaps each step




def pair_conflict(a, b):
   """Return True if truffles a and b (info lists) can't share a box."""
   # No two truffles exactly the same
   if a == b:
       return True
   # Caramel lovers don't like vanilla creme
   if {a[2], b[2]} == {"caramel", "vanilla"}:
       return True
   # Changed my mind: no toffee and coconut in the same box
   if {a[2], b[2]} == {"toffee", "coconut"}:
       return True
   # Nut lovers don't like sprinkles
   if {a[3], b[3]} == {"nuts", "sprinkles"}:
       return True
   # No white and dark chocolate drizzle in the same box
   if {a[3], b[3]} == {"white chocolate drizzle", "dark chocolate drizzle"}:
       return True
   # Boxes fit rectangles or squares, not both
   if {a[1], b[1]} == {"rectangle", "square"}:
       return True
   # New boxes: no round and heart shapes in the same box
   if {a[1], b[1]} == {"round", "heart"}:
       return True
   return False




def make_boxes(chocolates):
   """Split the truffles into boxes of 4 that follow all the rules.
   The friends "changed their minds" and now want 2-3 WHITE truffles,
   which may replace the old 2-3 DARK rule. So first try with every rule;
   if no answer turns up quickly, try again without the old dark rule."""
   boxes, solved = search(chocolates, use_dark_rule=True, time_limit=2)
   if solved:
       return boxes
   boxes2, solved2 = search(chocolates, use_dark_rule=False, time_limit=2.5)
   return boxes2 if solved2 else boxes




def search(chocolates, use_dark_rule, time_limit):
   """Start from random boxes and keep swapping truffles between boxes
   to remove rule violations. Returns (list of boxes, True if valid)."""
   ids = list(chocolates.keys())
   n_boxes = len(ids) // 4
   if n_boxes == 0:
       return [], True


   # Speed-up 1: truffles with identical info are the same "kind", so every
   # rule only has to be checked once per pair of kinds (not per pair of
   # truffles) and stored in a table.
   kind_of_info = {}
   kind = {}                     # truffle ID -> kind number
   kind_info = []                # kind number -> info list
   for t in ids:
       key = tuple(chocolates[t])
       if key not in kind_of_info:
           kind_of_info[key] = len(kind_info)
           kind_info.append(list(key))
       kind[t] = kind_of_info[key]
   n_kinds = len(kind_info)
   bad_pair = [[1 if pair_conflict(kind_info[x], kind_info[y]) else 0
                for y in range(n_kinds)] for x in range(n_kinds)]
   is_dark = [1 if info[0] == "dark" and use_dark_rule else 0
              for info in kind_info]
   is_white = [1 if info[0] == "white" else 0 for info in kind_info]


   def cost(a, b, c, d):
       """Rule violations for a box holding kinds a, b, c, d (0 = valid)."""
       ra, rb, rc = bad_pair[a], bad_pair[b], bad_pair[c]
       total = ra[b] + ra[c] + ra[d] + rb[c] + rb[d] + rc[d]
       # Boxes with dark (or white) chocolate need 2 or 3 of that kind
       dark = is_dark[a] + is_dark[b] + is_dark[c] + is_dark[d]
       white = is_white[a] + is_white[b] + is_white[c] + is_white[d]
       if dark == 1 or dark == 4:
           total += 1
       if white == 1 or white == 4:
           total += 1
       return total


   def box_cost(box):
       return cost(kind[box[0]], kind[box[1]], kind[box[2]], kind[box[3]])


   start = time.time()
   best_boxes, best_total = None, None
   # Restart from a new random arrangement if we stop making progress
   patience = max(3000, 60 * n_boxes)


   while time.time() - start < time_limit:
       random.shuffle(ids)
       boxes = [ids[i * 4:(i + 1) * 4] for i in range(n_boxes)]
       costs = [box_cost(b) for b in boxes]
       bad = set(i for i in range(n_boxes) if costs[i] > 0)
       run_best, since_improve, step = sum(costs), 0, 0


       while since_improve < patience:
           if not bad:
               return [sorted(b) for b in boxes], True
           total = sum(costs[i] for i in bad)
           if best_total is None or total < best_total:
               best_total = total
               best_boxes = [b[:] for b in boxes]
           if total < run_best:
               run_best, since_improve = total, 0
           else:
               since_improve += 1


           # Check the clock every so often (time.time() is slow-ish)
           step += 1
           if step % 200 == 0 and time.time() - start > time_limit:
               break


           i = random.choice(tuple(bad))
           if n_boxes == 1:
               break                      # nothing to swap with
           # Speed-up 2: only look at a random sample of other boxes
           others = [k for k in range(n_boxes) if k != i]
           if len(others) > SAMPLE:
               others = random.sample(others, SAMPLE)


           if random.random() < NOISE:
               # Random swap so the search doesn't get stuck
               p = random.randrange(4)
               j = random.choice(others)
               q = random.randrange(4)
           else:
               # Try every swap between box i and the sampled boxes
               ki = [kind[t] for t in boxes[i]]
               best_delta, moves = None, []
               for j in others:
                   kj = [kind[t] for t in boxes[j]]
                   base = costs[i] + costs[j]
                   for p in range(4):
                       x = ki[p]
                       ri = ki[:p] + ki[p + 1:]       # box i without slot p
                       for q in range(4):
                           y = kj[q]
                           if x == y:
                               continue               # swapping twins does nothing
                           rj = kj[:q] + kj[q + 1:]
                           delta = (cost(y, ri[0], ri[1], ri[2])
                                    + cost(x, rj[0], rj[1], rj[2]) - base)
                           if best_delta is None or delta < best_delta:
                               best_delta, moves = delta, [(p, j, q)]
                           elif delta == best_delta:
                               moves.append((p, j, q))
               if not moves:
                   continue
               p, j, q = random.choice(moves)


           boxes[i][p], boxes[j][q] = boxes[j][q], boxes[i][p]
           for k in (i, j):
               costs[k] = box_cost(boxes[k])
               if costs[k] > 0:
                   bad.add(k)
               else:
                   bad.discard(k)


       if n_boxes == 1:
           break


   # No perfect answer found in time: return the closest arrangement
   if best_boxes is None:
       best_boxes = [ids[i * 4:(i + 1) * 4] for i in range(n_boxes)]
   return [sorted(b) for b in best_boxes], False
