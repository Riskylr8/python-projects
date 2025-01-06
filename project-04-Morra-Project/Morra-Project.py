import random

# Menyambut pemain ke dalam permainan
print("Welcome to the Morra Game!")
print("The goal of the game is to correctly guess the total number of fingers shown by both players (your fingers + opponent's fingers).")

# Aturan permainan dan pengaturan jumlah ronde
rounds = int(input("How many rounds do you want to play? "))  # Meminta jumlah ronde dari pemain
player_score = 0  # Inisialisasi skor pemain
computer_score = 0  # Inisialisasi skor komputer

# Perulangan untuk setiap ronde permainan
for round_num in range(1, rounds + 1):
    print(f"\n--- Round {round_num} ---")  # Menampilkan nomor ronde

    # Pemain memilih jumlah jari yang akan ditampilkan (0 hingga 5)
    while True:
        try:
            user_choice = int(input("How many fingers do you choose (0 to 5)? "))
            if 0 <= user_choice <= 5:
                break  # Keluar dari loop jika input valid
            else:
                print("Invalid input. Please choose a number between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Komputer memilih jumlah jari secara acak (0 hingga 5)
    computer_choice = random.randint(0, 5)
    print(f"Computer chose: {computer_choice}")

    # Menghitung total jumlah jari
    total_fingers = user_choice + computer_choice
    print(f"Total fingers: {total_fingers}")

    # Pemain menebak total jumlah jari
    while True:
        try:
            user_guess = int(input("Guess the total number of fingers (0 to 10): "))
            if 0 <= user_guess <= 10:
                break  # Keluar dari loop jika input valid
            else:
                print("Invalid input. Please guess a number between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Komputer menebak total jumlah jari secara acak (0 hingga 10)
    computer_guess = random.randint(0, 10)
    print(f"Computer guessed: {computer_guess}")

    # Menentukan pemenang untuk ronde ini
    if user_guess == total_fingers and computer_guess == total_fingers:
        print("It's a tie! Both guessed correctly!")
        player_score += 1
        computer_score += 1
    elif user_guess == total_fingers:
        print("You win this round! You guessed the total correctly.")
        player_score += 1
    elif computer_guess == total_fingers:
        print("Computer wins this round! It guessed the total correctly.")
        computer_score += 1
    else:
        print("No one guessed the total correctly this round.")

    # Menampilkan skor saat ini
    print(f"Scores: You - {player_score}, Computer - {computer_score}")

# Menampilkan hasil akhir permainan
print("\n=== Game Over ===")
if player_score > computer_score:
    print(f"Congratulations! You win the game with a score of {player_score} to {computer_score}.")
    print("\U0001F604")  # Wajah tersenyum
elif player_score < computer_score:
    print(f"Computer wins the game with a score of {computer_score} to {player_score}. Better luck next time!")
    print("\U0001F622")  # Wajah sedih
else:
    print(f"It's a tie! Both scored {player_score}.")
    print("\U0001F610")  # Wajah netral
