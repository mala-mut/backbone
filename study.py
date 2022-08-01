TICKET_PRICE = 10
PRICE = 15
MAIN_MENU = """What would you like to do?
(1) How many tickets are left?
(2) Buy tickets
(0) Exit
"""

tickets_remaining = 100
answer = ""

name = input('What is your name?\n')
print(f'Hi, {name}!')

while answer != "0" and tickets_remaining:
    answer = input(MAIN_MENU)
    if answer == "1":
        print(f'There are {tickets_remaining} remaining')
    elif answer == "2":
        try:
            tickets_bought = int(input('How many tickets would you like?\n'))
        except ValueError:
            print("That doesn't seem to be the number of tickets, try again :(")
        else:
            if tickets_bought > tickets_remaining:
                print(f'There are only {tickets_remaining} remained!')
                continue
            print(f'It will cost ${PRICE * tickets_bought}')
            confirmation = input("""Would you like to buy it?
            (Answer yes/no)
            """)
            if confirmation == 'yes' and tickets_bought < tickets_remaining:
                print(f'Here are your {tickets_bought} tickets!')
                tickets_remaining -= int(tickets_bought)
            else:
                print('Ok then')

print('Have a good day!')
