'''
This is broken but good enough to demonstrate you understand OOP
'''


"""
DESIGN A PARKING GARAGE THAT HAS 3 PARKING SIZES AND GIVES A TICKET.
CREATE A CAR REPRESENTING THE OBJECT PAYING AND OBTAINING A SLOT.
CREATE A CLASS THAT SERVES AS A TICKET
"""

options = list(
    [first_tier := "Compact", second_tier := "Standard", third_tier := "Handicap"]
)
error_message = (
    f"Sorry you have selected an invalid choice. Please choose between {options}"
)


def invalid_choice():
    raise ValueError(error_message)


class ParkingGarage:
    def __init__(self, size: str) -> None:
        if size.title() not in options:
            invalid_choice()
        else:
            self.size = size

    def confirm_choice(self) -> int | str:
        confirm_choice = input(
            f"You have purchased the {first_tier} size. Would you like to continue"
        )
        if confirm_choice.lower() != "y":
            return f"Please, make a new selection"
        else:
            return self.size

    def parking_size(self) -> None:
        if self.size in options:
            return self.confirm_choice()
        else:
            invalid_choice()


class Ticket:
    def __init__(self, size: ParkingGarage.parking_size) -> None:
        self.size = size.lower()

        if self.size == first_tier.lower():
            self.price = 15
        elif self.size == second_tier.lower():
            self.price = 20
        elif self.size == third_tier.lower():
            self.price = 25
        else:
            invalid_choice()

    def __repr__(self) -> tuple[str, int]:
        # return f"You have been charged {self.price}. Thank you for your purchase!"
        return (self.size, self.price)


def insufficient_funds(balance):
    return f"Sorry, this would being your balance to {balance}. You need more money."


class Car:
    def __init__(self, ticket: Ticket, balance) -> None:
        self.model = "Chevrolet Camaro"
        self.license = "LNDO"
        self.balance = balance - ticket[1]
        self.slot = None

        if self.balance >= 0:
            self.slot = ticket[0]
        else:
            print(insufficient_funds(self.balance))

    def __repr__(self) -> str:
        return f"{self.model}, license: {self.license} has been assigned {self.slot}"


garage = ParkingGarage(size="Compact")
slot = garage.parking_size()
ticket = Ticket(slot)
print(str(ticket[0]))
# my_car = Car(ticket=ticket, balance=100)
# print(my_car)
