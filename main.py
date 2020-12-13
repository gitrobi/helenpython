# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def reversewords(input):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    inputwords=input.split(" ")
    inputwords=inputwords[-1: :-1]
    output=''.join(inputwords)
    return output

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
   input='I like runoob'
   rw=reversewords(input)
   print(rw)