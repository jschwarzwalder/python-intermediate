colors = ['red', 'green', 'blue', 'purple', 'pink', 'yellow']
print( [ color.upper() for color in colors])

#  first 5 multiples of 3
#  [0, 3, 6, 9, 12]
print ([ n*3 for n in range(5)])

#[3, 2, 1, 0 , 1, 2]
print ([ abs(x) for x in range (-3, 3)])

def is_palindrome(s):
    return s== s[::-1]

words = ["bias", "moon", "dad", "eye", "deer", "racecar", "A santa at Nasa"]
palindroms = [ word for word in words if is_palindrome(word)]
print (palindroms)