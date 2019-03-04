#Lane Snively
#COSC2030, Lab03
#March 04, 2019
#I received help from everyone in the lab section

import operator
ops = {
       '+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.truediv,
       '^':operator.pow
       }

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def calculate(exp):
    stack = []
    result = 0
    for i in exp:
        if is_number(i):
            #stack.insert(0,i)
            stack.append(i)
        else:
            if len(stack) < 2:
                print ('Error: insufficient values in expression')
                break
            else:
                print ('stack: ', stack, 'where i = ', i)
                #operand1 = float(stack.pop(1))
                #operand2 = float(stack.pop(0))
                operand1 = float(stack.pop())
                operand2 = float(stack.pop())
                if (i=='/' or i=='^'):
                    ops[i](operand2,operand1)
                else:
                    ops[i](operand1,operand2)
                #stack.insert(0,str(result))
                stack.append(str(result))
    return result

print ("Start of Polish Notation Evaluator")
exp_file = open("Expressions1regular.txt", 'r')
for line in exp_file:
        exp_list = line.rstrip().split(' ')
        answer = calculate(exp_list)
        print ('RESULT: %f' % answer)
print ("End of Polish Notation Evaluator")
