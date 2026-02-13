import random

# Corrigido: "papper" para "paper"
options = ["rock", "paper", "scissors"]

# Loop para garantir que o usuário escolha uma opção válida
while True:
    # Corrigido: adicionado () ao .lower()
    user_choice = input("Make your choice (rock, paper, or scissors): ").lower()
    if user_choice in options:
        break # Sai do loop se a escolha for válida
    else:
        print("Invalid choice. Please try again.")

computer_choice = random.choice(options)

# Corrigido: adicionado 'f' para f-strings e corrigidos os nomes das variáveis
print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie! 🤝")
# Corrigido: "scissor" para "scissors" e "papper" para "paper"
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("You win! 🎉")
else:
    print("The computer wins! 🤖")