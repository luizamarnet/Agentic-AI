
def print_name():
    print("helper 1")


try:
    input_val = input("Give me a number: ")
    input_val = int(input_val)
    print(input_val*2)
except ValueError as e:
    print(f"Only numers accepted. Type {type(input_val)} given by user!!!")