#import random

#print(random.randint(5, 20))  # line 1
#print(random.randrange(3, 10, 2))  # line 2
#print(random.uniform(2.5, 5.5))  # line 3

"""

What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

I saw an integer produced, smallest I saw is 9 and largest I saw is 19

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?

I saw an integer as well, smallest I saw is 3 and largest I saw is 9
line 2 only produces 3 and numbers added by 2, so 3 5 7 9 are possible outcomes

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

I saw a long decimal number produced, 3.28009194367529 was the smallest, 5.1082581336545045
was the largest
"""

import random

random_number = random.randint(1, 100)
print(random_number)