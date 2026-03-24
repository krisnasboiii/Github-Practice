import random

All_Avengers = {
    "ironman": "Tony Stark",
    "captain_america": "Steve Rogers",
    "thor": "Thor Odinson",
    "hulk": "Bruce Banner",
    "black_widow": "Natasha Romanoff",
    "hawkeye": "Clint Barton",
    "spiderman": "Peter Parker",
    "black_panther": "T'Challa",
    "ant_man": "Scott Lang",
    "thanos": "Thanos"
}

# Functions

def show_all():
    print("\n--- All Avengers ---")
    for hero, real in All_Avengers.items():
        print(f"{hero.title()} -> {real}")


def search_hero():
    name = input("Enter Avenger name: ").lower()
    if name in All_Avengers:
        print("Real name:", All_Avengers[name])
    else:
        print("Avenger not found ❌")


def reverse_search():
    real_name = input("Enter real name: ").lower()
    found = False
    for hero, real in All_Avengers.items():
        if real.lower() == real_name:
            print("Hero is:", hero.title())
            found = True
            break
    if not found:
        print("Not found ❌")


def random_hero():
    hero = random.choice(list(All_Avengers.keys()))
    print("Random Avenger:", hero.title())


def quiz_game():
    hero, real = random.choice(list(All_Avengers.items()))
    answer = input(f"What is the real name of {hero.title()}? ")
    if answer.lower() == real.lower():
        print("Correct 😎")
    else:
        print("Wrong ❌ Correct answer:", real)


def team_generator():
    team = random.sample(list(All_Avengers.keys()), 3)
    print("Your Team:", [hero.title() for hero in team])


def add_avenger():
    hero = input("Enter hero name: ").lower()
    real = input("Enter real name: ")
    All_Avengers[hero] = real
    print("Avenger added successfully ✅")


# Main Menu

while True:
    print("\n====== AVENGERS MENU ======")
    print("1. Show All Avengers")
    print("2. Search Avenger")
    print("3. Reverse Search (Real Name -> Hero)")
    print("4. Random Avenger")
    print("5. Quiz Game")
    print("6. Generate Team")
    print("7. Add New Avenger")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_all()
    elif choice == "2":
        search_hero()
    elif choice == "3":
        reverse_search()
    elif choice == "4":
        random_hero()
    elif choice == "5":
        quiz_game()
    elif choice == "6":
        team_generator()
    elif choice == "7":
        add_avenger()
    elif choice == "8":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice ❌")