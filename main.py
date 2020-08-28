"""Write a function called sample_percent that takes four parameters. This first parameter, obs_list, will be a list of observations. The second, third, and fourth parameters are called group1, group2, and group3 and are objects whose counts should be recorded. The function should return a list where each item is a percentage of the count of its respective group relative to the total number of elements in the obs_list.

Here is an example of how this function should work:

example_lst = ['dog', 'cat', 'dog', 'fish']
sample_percent(example_lst, 'dog', 'cat', 'fish')

# Should return
[.5, .25, .25]
"""

obs_list = ['dog', 'cat', 'dog', 'fish']

group1 = 'dog'

group2 = 'cat'

group3 = 'fish'

def sample_percent(obs_list, group1, group2, group3):
  group1_percent = (obs_list.count(group1))/(len(obs_list))
  group2_percent = (obs_list.count(group2))/(len(obs_list))
  group3_percent = (obs_list.count(group3))/(len(obs_list))
  percent_list = [group1_percent, group2_percent, group3_percent]

  return percent_list

print(sample_percent(obs_list, group1, group2, group3))