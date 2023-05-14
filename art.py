# Rock Paper Scissors ASCII Art

def main():
    print(draw(input("Choice: ")))


def draw(choice):
    #Rock
    if choice == "Rock":
        return """
            _______
        ---'   ____)
             (_____)
             (_____)
              (____)
        ---.__(___)
        """
    
    elif choice == "Paper":
        # Paper
        return """
            _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """
    
    elif choice == "Scissor":
        # Scissors
        return """
            _______
        ---'   ____)____
                  ______)
              __________)
              (____)
        ---.__(___)
        """
    
    elif choice == "Spock":
        return """  
                         ___
                 ___    |   |___
             ___|   |   |   |   |
            |   |   |   |   |   |
            |   |   |   |   |   |
            |   |   |   |   |   |    ___
            |   |    \_/    |   |   /   |
            |                   |  /    |
            |                    \/    |
            |                         |
            |                        /
            |                       / 
             \                     / 
              \__________________ /


            """
    elif choice == "Lizard":
        return """
                _____________________  
               /_____________________) 
              /            ___________)
        _____/           / 
                        |
        _____            \______/  )    
             \____________________/
        
        """

if __name__ == "__main__":
    main()