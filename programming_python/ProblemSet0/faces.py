def main():
    message = str(input())
    print(convert(message))

#def convert is a function allowing to replace :) by 🙂 and :( by 🙁
def convert (smiley):
    return smiley.replace(':)','🙂').replace(':(','🙁')

main()
