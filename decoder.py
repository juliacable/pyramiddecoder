message_file = open('content.txt', 'r') # make python open and read the txt file
nums_in_txt = [] # holds the numbers from the txt file
rightmostnums = [] # holds the rightmost numbers in the 'pyramid'

def populate(file_txt):
    list_lines = [] # list of each line in the txt file
    keydict = {} # empty dictionary to store key value pairs
    list_lines = file_txt.readlines()
    for item in list_lines:
        splititem = item.split()
        nums_in_txt.append(int(splititem[0])) # populates list of numbers
        keydict[int(splititem[0])] = splititem[1] # populating dictionary with key value pairs
    return keydict

def create_staircase(nums): 
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
  return subsets

def get_final_elements(list_of_lists): # gets last element of 'pyramid' layer
   for element in list_of_lists:
      rightmostnums.append(element[len(element) - 1]) 

def decode(message_file):
   dictionary = populate(message_file)
   sorted_txt_nums = sorted(nums_in_txt)
   staircase = create_staircase(sorted_txt_nums) # makes the pyramid
   get_final_elements(staircase)
   for num in rightmostnums: # uses the list of rightmost elements
      print(dictionary[num]) # prints the word associated with the number

decode(message_file)