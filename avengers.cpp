#include <iostream>
using namespace std;

int main() {
    int choice;

    cout << "=============================\n";
    cout << "   AVENGERS CONTROL PANEL   \n";
    cout << "=============================\n";
    cout << "1. Iron Man\n";
    cout << "2. Captain America\n";
    cout << "3. Thor\n";
    cout << "4. Hulk\n";
    cout << "5. Exit\n";
    cout << "Choose your Avenger: ";
    cin >> choice;

    cout << "\n";

    switch(choice) {
        case 1:
            cout << "Iron Man 🦾\n";
            cout << "Power: Genius, Billionaire, Suit Technology\n";
            break;

        case 2:
            cout << "Captain America 🛡️\n";
            cout << "Power: Super Soldier, Shield Master\n";
            break;

        case 3:
            cout << "Thor ⚡\n";
            cout << "Power: God of Thunder, Lightning Control\n";
            break;

        case 4:
            cout << "Hulk 💪\n";
            cout << "Power: Super Strength, Rage Mode\n";
            break;

        case 5:
            cout << "Exiting Avengers Panel...\n";
            break;

        default:
            cout << "Invalid Choice! Try Again.\n";
    }

    return 0;
}