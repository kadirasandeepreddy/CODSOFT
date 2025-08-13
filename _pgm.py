def add(a,b):
    return a+b
def subract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operation_dict={
    "+":add,
    "-":subract,
    "*":multiply,
    "/":divide
}
number1=int(input("enter the number"))
for symbol in operation_dict:
    print(symbol)
op_symbol=input("pick ana operation:")
number2=int(input("enter the number2"))
calculator_function=operation_dict[op_symbol]
output=calculator_function(number1,number2)
print(f"{number1} {op_symbol} {number2} = {output}")