def calculadora(operacao):

    def soma(a,b):
        return a + b
    
    def sub(a,b):
        return a - b
    
    def mult(a,b):
        return a * b
    
    def div(a,b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mult
        case "/":
            return div
    # or
    # if operacao == "+":
    #     return soma
    # elif operacao == "-": 
    #     return sub
    # elif operacao == "*":
    #     return mult
    # else:
    #     return div


print(calculadora("+"))
print(calculadora("-"))
print(calculadora("*"))
print(calculadora("/"))

calculadora_obj = calculadora("/")

print(calculadora_obj(2,3))


