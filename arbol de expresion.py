class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def infix_to_postfix(expression):
    """Convierte una expresión en notación infija a postfija utilizando el algoritmo Shunting-yard."""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    num = ''
    for c in expression:
        if c.isdigit():
            num += c
        else:
            if num:
                output.append(num)
                num = ''
            if c in '+-*/':
                while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[c]:
                    output.append(stack.pop())
                stack.append(c)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack: 
                    stack.pop()  # Quitar el '('
    if num:
        output.append(num)
    while stack:
        output.append(stack.pop())
    return output

def build_tree(expression):
    """
    Construye el árbol de expresión a partir de la conversión de infijo a postfijo.
    Se utiliza una pila para asignar nodos.
    """
    postfix = infix_to_postfix(expression)
    stack = []
    for token in postfix:
        if token.isdigit():
            node = Node(token)
            stack.append(node)
        else:
            node = Node(token)
            # El último elemento de la pila es el hijo derecho.
            node.right = stack.pop() if stack else None
            # Luego se obtiene el hijo izquierdo.
            node.left = stack.pop() if stack else None
            stack.append(node)
    return stack[0] if stack else None

def print_ascii_tree(node, prefix="", is_left=True):
    """
    Imprime el árbol de forma gráfica utilizando líneas ASCII.
    El árbol se muestra "rotado" 90° para visualizar las ramas.
    """
    if node.right:
        new_prefix = prefix + ("│   " if is_left else "    ")
        print_ascii_tree(node.right, new_prefix, False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
    if node.left:
        new_prefix = prefix + ("    " if is_left else "│   ")
        print_ascii_tree(node.left, new_prefix, True)

# Ejemplo de uso:
expression = input("Introduce la expresión (por ejemplo 3*(9-3*4)): ")
tree = build_tree(expression)
print("\nÁrbol de expresiones:")
print_ascii_tree(tree)