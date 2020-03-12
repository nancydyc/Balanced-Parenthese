"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

    # loop over the string
    # if see an open paren, add to a list
    # if see a closing paren, remove the last open paren for balance
    # meanwhile, if no open paren to remove for balance, return False for unbalance--extra ")"
    # When loop is done, if there's no open paren left, return True for balance, 
    # else return False for unbalance--extra "(".

    parens = []

    for i in phrase:
      if i == "(":
        parens.append(i)

      if i == ")" and parens != []:
        parens.pop()
      # use elif to make sure this condition happens at the same time as above, not after  
      elif i == ")" and parens == []: 
        return False

    if parens == []:
      return True

    else:
      return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
