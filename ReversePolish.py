#################################################################
#
#
# TODO：如何处理 sin(A) 这样的表达式
#
#
#
#
#
#
#
#################################################################



#定义运算符栈
operator_stack = []
#定义操作数栈
operand_stack = []

#定义哪些是运算符
operators = ('+', '-', '*', '/', '(', ')',)
#优先级
priority = {'+':1, '-':1, '*':2, '/':2, '(':3, ')':0}
#定义哪些是操作数
operands = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

######TEMP###################
ex = '1+4-3'
length = len(ex)
#############################

######################################
#第一步应该检查是不是表达式是不是符合规范
######################################

i = 0
while i < length:
    cur = ex[i]
    i += 1
    if cur in operators:
        if len(operator_stack) == 0 or cur == '(':
            operator_stack.append(cur)
        else:
            if cur == ')':
                top = operator_stack.pop()
                while top != '(':
                    operand_stack.append(top)
                    top = operator_stack.pop()
            else:
                top = operator_stack[-1]
                if priority[cur] >= priority[top] or top == '(':
                    operator_stack.append(cur)
                else:
                    top = operator_stack.pop()
                    operand_stack.append(top)
                    operator_stack.append(cur)
    elif cur in operands:
        operand_stack.append(cur)
    else:
        continue

#最后将运算符全部出栈并添加到操作数栈中
while operator_stack:
    operand_stack.append(operator_stack.pop())

print(operand_stack)


result_statck = []
while operand_stack:
    cur = operand_stack.pop(0)
    if cur in operands:
        result_statck.append(cur)
    elif cur in operators:
        o2 = float(result_statck.pop())
        o1 = float(result_statck.pop())
        temp = 'NULL'
        if cur == '+':
            temp = o1 + o2
        elif cur == '-':
            temp = o1 - o2
        elif cur == '*':
            temp = o1 * o2
        elif cur == '/':
            temp = o1 / o2
        if temp != 'NULL':
            result_statck.append(temp)

result = result_statck.pop()
print(result)
