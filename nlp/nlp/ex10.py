from pywsd.lesk import simple_lesk
sentences = ['I went to the bank to deposit money','The river bank was full of fishes']
print('Context1 : ',sentences[0])
answer = simple_lesk(sentences[0],'bank')
print('Sense : ',answer)
print('Definition : ',answer.definition())
print('Context2 : ',sentences[1])
answer = simple_lesk(sentences[1],'bank')
print('Sense : ',answer)
print('Definition : ',answer.definition())