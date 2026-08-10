import random

print("=" * 50)
print("        🎯 SMART NUMBER GUESSING GAME")
print("=" * 50)

best_score = 0
games_played = 0

while True:

    print("\n🎮 SELECT DIFFICULTY")
    print("-" * 35)
    print("1. Easy   🟢  (1 - 50)   | 10 Attempts")
    print("2. Medium 🟡  (1 - 100)  | 7 Attempts")
    print("3. Hard   🔴  (1 - 500)  | 10 Attempts")
    print("-" * 35)

    while True:
        difficulty = input("Choose difficulty (1/2/3): ")

        if difficulty == "1":
            max_number = 50
            max_attempts = 10
            level = "Easy 🟢"
            break

        elif difficulty == "2":
            max_number = 100
            max_attempts = 7
            level = "Medium 🟡"
            break

        elif difficulty == "3":
            max_number = 500
            max_attempts = 10
            level = "Hard 🔴"
            break

        else:
            print("❌ Invalid choice! Enter 1, 2 or 3.")

    secret_number = random.randint(1, max_number)
    attempts = 0
    hints_used = 0

    print("\n" + "=" * 50)
    print(f"🔥 {level} MODE ACTIVATED!")
    print(f"I'm thinking of a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts.")
    print("Type 'H' for a hint.")
    print("=" * 50)

    while attempts < max_attempts:

        print(f"\n❤️  Attempts left: {max_attempts - attempts}")

        user_input = input("🎯 Enter your guess: ").strip().lower()

        # Hint
        if user_input == "h":

            if hints_used >= 2:
                print("💡 You have already used the maximum 2 hints!")

            else:
                hints_used += 1

                if secret_number % 2 == 0:
                    print("💡 Hint: The number is EVEN.")
                else:
                    print("💡 Hint: The number is ODD.")

                
                if hints_used == 2:

                    if secret_number <= max_number // 2:
                        print(
                            f"💡 Extra Hint: The number is between "
                            f"1 and {max_number // 2}."
                        )
                    else:
                        print(
                            f"💡 Extra Hint: The number is between "
                            f"{max_number // 2 + 1} and {max_number}."
                        )

            continue

        
        if not user_input.isdigit():
            print("❌ Please enter a number or type H for a hint.")
            continue

        guess = int(user_input)

        if guess < 1 or guess > max_number:
            print(f"⚠️ Enter a number between 1 and {max_number}.")
            continue

        attempts += 1

        
        if guess == secret_number:

            games_played += 1

            
            score = (
                (max_attempts - attempts + 1) * 100
                - (hints_used * 25)
            )

            if score < 0:
                score = 0

            print("\n" + "=" * 50)
            print("           🎯 JACKPOT! 🎯")
            print("=" * 50)
            print(f"✅ Correct Number: {secret_number}")
            print(f"🎮 Attempts Used: {attempts}")
            print(f"💡 Hints Used: {hints_used}")
            print(f"🏆 Your Score: {score}")

            
            if score > best_score:
                best_score = score
                print("👑 NEW HIGH SCORE!")
            else:
                print(f"🥇 Best Score: {best_score}")

            print("=" * 50)

            break

        
        elif guess < secret_number:

            difference = secret_number - guess

            if difference <= 5:
                print("🔥 VERY CLOSE! Your guess is too LOW.")
            else:
                print("🔼 Too LOW! Try a bigger number.")

        
        else:

            difference = guess - secret_number

            if difference <= 5:
                print("🔥 VERY CLOSE! Your guess is too HIGH.")
            else:
                print("🔽 Too HIGH! Try a smaller number.")


    else:

        games_played += 1

        print("\n" + "=" * 50)
        print("             💀 GAME OVER")
        print("=" * 50)
        print(f"The secret number was: {secret_number}")
        print("Better luck next time! 💪")
        print("=" * 50)

    # Game statistics
    print("\n📊 GAME STATISTICS")
    print("-" * 30)
    print(f"🎮 Games Played : {games_played}")
    print(f"🏆 Best Score   : {best_score}")


    while True:

        play_again = input(
            "\n🔄 Do you want to play again? (Y/N): "
        ).strip().lower()

        if play_again == "y":
            print("\n🚀 Starting a new game...")
            break

        elif play_again == "n":
            print("\n" + "=" * 50)
            print("     👋 THANKS FOR PLAYING!")
            print(f"     🏆 Final Best Score: {best_score}")
            print(f"     🎮 Total Games: {games_played}")
            print("=" * 50)
            print("🔥 Keep Coding! Keep Building! 🚀")
            exit()

        else:
            print("❌ Invalid input! Please enter Y or N.")