
#main function
def main():
    name = input("What's your name ? ")
    hello(name)


#######################################

#def function named hello with "to" as a parameter
def hello(to):
    print("hello ,", to) #=> "to" here is the argument

#call main function in order to use the function "hello" in our main code
main()
