def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    n1=float(input("Enter your First Number: "))
    for symbol in operations:
        print(symbol)
    operation=input("Enter Operation do you want to apply: ")
    n2=float(input("Enter your Second Number: "))
    answer=operations[operation](n1,n2)
    print(f"answer={answer}")
calculator()
