def main():
    print('This program converts dollrs to pounds sterling')
    print()

    dollars = eval(input('Enter ammount in dollars: '))

    pounds = convert_to_pounds(dollars)

    print('That is', pounds, 'pounds.')

convert_to_pounds = lambda dollars: dollars* 0.82

main()