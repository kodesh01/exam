import re
def regex(pattern,text):
    matches = re.findall(pattern,text)
    if len(matches)!=0:
        print("Word patterns detected")
        for word in matches:
            print(word,end='')
        print('')
inputs=[('[0-9]','The pen is 10 rupees'),
        ('[A-za-z]','Spain123')]
for pattern,text in inputs:
    print(pattern)
    print(text)
    regex(pattern,text)
    print('------------')