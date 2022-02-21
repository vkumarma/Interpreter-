import parser
import main
import sys

tokens = main.tokens_list
tokens_dict = main.tokens()
tree = parser.parse_tree()

def scanned_tokens(): # printing scanned tokens
    for token in tokens:
        output_file.write(token + ":" + tokens_dict[token] + "\n")
    output_file.write("\n")


def preorder(tree, indent): # printing parse tree.
    if tree != None:
        write_string = indent + tree.root + ":" + tokens_dict[tree.root] + "\n"
        output_file.write(write_string)
        # print(indent, tree.root, ":", tokens_dict[tree.root])
        indent += "         "
        preorder(tree.left, indent)
        if tree.center != None:
            preorder(tree.center, indent)
        preorder(tree.right, indent)



stack = []
def evaluator(tree,stack):
    result = 0
    if tree != None:
        if len(stack) > 2:
            while stack[len(stack)-1].isdigit() and stack[len(stack)-2].isdigit():
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                op = stack.pop()
                if op == "+":
                    result = num2 + num1
                elif op == "-":
                    result = num2 - num1
                    if result < 0:
                        result = 0
                elif op == "/":
                    if num1 == 0:
                        raise Exception
                    result = num2 // num1
                elif op == "*":
                    result = num2 * num1
                stack.append(str(result))

        stack.append(tree.root)
        evaluator(tree.left, stack)
        evaluator(tree.right, stack)


def evaluation():
    result = 0
    while len(stack) != 1:
        if stack[len(stack) - 1].isdigit() and stack[len(stack) - 2].isdigit():
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            op = stack.pop()
            if op == "+":
                result = num2 + num1
            elif op == "-":
                result = num2 - num1
                if result < 0:
                    result = 0
            elif op == "/":
                if num1 == 0:
                    raise Exception
                result = num2 // num1
            elif op == "*":
                result = num2 * num1
            stack.append(str(result))

    return stack



##################################################### Functions called #########
output_file = open(str(sys.argv[2]), 'w')
output_file.write("Tokens: \n")
output_file.write("\n")
scanned_tokens()
output_file.write("AST: \n")
output_file.write("\n")
preorder(tree, "")
output_file.write("\n")
evaluator(tree, stack)
output = evaluation()[0]
output_file.write("\n")
output_file.write("Output: " + str(output))