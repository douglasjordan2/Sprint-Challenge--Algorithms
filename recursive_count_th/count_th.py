'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  # break case. once the length of the word we're passing in is less than 1 we just return a 0
  if len(word) < 1:
    return 0

  # here we check if the first 2 letters are th. if they are, we return 1 + a recursive call to this function where we pass in the same word but we get rid of the 1st letter (if the first 2 letters are not th, then we add 0). as the function keeps calling itself, it grows to have a chain of 1 + 0 + 0 + 1 + 0... (just an example). this return statement keeps growing, adding 1 or 0, until it reaches the break case with 0, adds all the values prepared in the return, and returns the amount of times th is found in the word.

  # because the function is acting on the length of the word and subtracting 1 letter with each pass, the runtime complexity is O(n)

  if word[:2] == 'th':
    return 1 + count_th(word[1:])
  else:
    return 0 + count_th(word[1:])


# small change