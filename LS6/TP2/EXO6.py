def is_balanced(s) :
    stack=[]
    for i in s:
        if i.isalpha():
            stack.append(i)
            stack.pop()
        if i=='(' or i=='[' :
            stack.append(i)
        elif i==')':
            if stack[-1]=='(':
                stack.pop()
            else :
                stack.append(i)
        elif i==']':
            if stack[-1]=='[':
                stack.pop()
            else :
                stack.append(i)
    return len(stack)==0

print (is_balanced("([aa](bb[]))")) # True
print (is_balanced("([aa)](bb[])")) # False
print (is_balanced("([aa](bb[])")) # False

