#!/bin/bash

# Mini Elden Ring-based game that lets the user fight a standard beast and Margit, the Fell Omen.
# Uses random numbers to decide if the Tarnished won/lost the fight.


# Clear screen and display the class selection menu to the user.
clear
echo "Welcome Tarnished. Please select your starting class:

1. Hero
2. Bandit
3. Astrologer
4. Warrior
5. Prisoner
6. Confessor
7. Wretch
8. Vagabond
9. Prophet
10. Samurai
0. Exit

"
read -p "Class: " CLASS
clear

case $CLASS in
    1)
        echo "Class: Hero"
        echo "Vgr: 14"
        echo "Mnd: 9"
        echo "End: 12"
        echo "Str: 16"
        echo "Dex: 9"
        echo "Int: 7"
        echo "Fth: 8"
        echo -e "Arc: 11\n"
        ;;
    2)
        echo "Class: Bandit"
        echo "Vgr: 10"
        echo "Mnd: 11"
        echo "End: 10"
        echo "Str: 9"
        echo "Dex: 13"
        echo "Int: 9"
        echo "Fth: 8"
        echo -e "Arc: 14\n"
        ;;
    3)
        echo "Class: Astrologer"
        echo "Vgr: 9"
        echo "Mnd: 15"
        echo "End: 9"
        echo "Str: 8"
        echo "Dex: 12"
        echo "Int: 16"
        echo "Fth: 7"
        echo -e "Arc: 9\n"
        ;;
     4)
        echo "Class: Warrior"
        echo "Vgr: 11"
        echo "Mnd: 12"
        echo "End: 11"
        echo "Str: 10"
        echo "Dex: 16"
        echo "Int: 10"
        echo "Fth: 8"
        echo -e "Arc: 9\n"
        ;;
    5)
        echo "Class: Prisoner"
        echo "Vgr: 11"
        echo "Mnd: 12"
        echo "End: 11"
        echo "Str: 11"
        echo "Dex: 14"
        echo "Int: 14"
        echo "Fth: 6"
        echo -e "Arc: 9\n"
        ;;
    6)
        echo "Class: Confessor"
        echo "Vgr: 10"
        echo "Mnd: 13"
        echo "End: 10"
        echo "Str: 12"
        echo "Dex: 12"
        echo "Int: 9"
        echo "Fth: 14"
        echo -e "Arc: 9\n"
        ;;
    7)
        echo "Class: Wretch"
        echo "Vgr: 10"
        echo "Mnd: 10"
        echo "End: 10"
        echo "Str: 10"
        echo "Dex: 10"
        echo "Int: 10"
        echo "Fth: 10"
        echo -e "Arc: 10\n"
        ;;
    8)
        echo "Class: Vagabond"
        echo "Vgr: 15"
        echo "Mnd: 10"
        echo "End: 11"
        echo "Str: 14"
        echo "Dex: 13"
        echo "Int: 9"
        echo "Fth: 9"
        echo -e "Arc: 7\n"
        ;;
    9)
        echo "Class: Prophet"
        echo "Vgr: 10"
        echo "Mnd: 14"
        echo "End: 8"
        echo "Str: 11"
        echo "Dex: 10"
        echo "Int: 7"
        echo "Fth: 16"
        echo -e "Arc: 10\n"
        ;;
    10)
        echo "Class: Samurai"
        echo "Vgr: 12"
        echo "Mnd: 11"
        echo "End: 13"
        echo "Str: 12"
        echo "Dex: 15"
        echo "Int: 9"
        echo "Fth: 8"
        echo -e "Arc: 8\n"
        ;;
    0)
        echo -e "You Died\n"
        exit 1
        ;;
    *)
        echo -e "Invalid option. Terminating script...\n"
        exit 1
        ;;
esac


# First beast battle

BEAST=$(( $RANDOM % 2 ))

read -p "Your first beast approaches. Prepare to battle. Pick a number (0-1): " TARNISHED

if [[ $BEAST == $TARNISHED ]]; then
    echo -e "BEAST VANQUISHED\n"
else
    echo -e "You Died\n"
    exit 1
fi

echo -e "Resting...\n"
sleep 2

# Margit, the Fell Omen

MARGIT=$(( $RANDOM % 10 ))

read -p "Margit, the Fell Omen approaches. Prepare to battle. Pick a number between 0-9: " TARNISHED

if [[ $MARGIT == $TARNISHED || $TARNISHED == "cheater" ]]; then
    echo -e "GREAT ENEMY FELLED\n"
else
    echo -e "You Died\n"
fi

