class UI:
    def __init__(self):
        pass
    def main_menu(self):
        """
        Diplays the menu options for player to choose
        return: str
        """
        print(""".___  ___.   ______   ____    ____  __   _______     _______       ___   .___________.    ___      .______        ___           _______. _______ 
|   \/   |  /  __  \  \   \  /   / |  | |   ____|   |       \     /   \  |           |   /   \     |   _  \      /   \         /       ||   ____|
|  \  /  | |  |  |  |  \   \/   /  |  | |  |__      |  .--.  |   /  ^  \ `---|  |----`  /  ^  \    |  |_)  |    /  ^  \       |   (----`|  |__   
|  |\/|  | |  |  |  |   \      /   |  | |   __|     |  |  |  |  /  /_\  \    |  |      /  /_\  \   |   _  <    /  /_\  \       \   \    |   __|  
|  |  |  | |  `--'  |    \    /    |  | |  |____    |  '--'  | /  _____  \   |  |     /  _____  \  |  |_)  |  /  _____  \  .----)   |   |  |____ 
|__|  |__|  \______/      \__/     |__| |_______|   |_______/ /__/     \__\  |__|    /__/     \__\ |______/  /__/     \__\ |_______/    |_______|
""")
        print("1. Queries")
        print("2. Update Database")
        print("X. Quit\n")
        print("Please choose an option (1 or X)")
        while True:
            response = input("> ").upper()
            if response in ["1", "2", "X"]:
                return response
            else:
                print("Incorrect choice\n")

    def query_menu(self):
        """
        Displays the query options
        return: str
        """
        print("Query Menu")
        print("==========")
        print("1. List countries")
        print("2. List memebers")
        print("3. List movies")
        print("4. List directors by country")
        print("5. List member details")
        print("6. List movies a member has on hire")
        print("7. List movies a director has directed")
        print("8. List all movie details")
        print("9. List all loan details")
        print("Q. Return to main menu\n")
        print("Please choose an option (A to I or X)")
        while True:
            response = input("> ").upper()
            if response in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Q"]:
                return response
            else:
                print("Incorrect choice\n")

    def update_menu(self):
        """
        Displays the update options
        return: str
        """
        print("Update Menu")
        print("==========")
        print("1. Add member")
        print("Q. Return to main menu\n")
        print("Please choose an option (1 to 6 or Q)")
        while True:
            response = input("> ").upper()
            if response in ["1", "2", "3", "4", "5", "6", "Q"]:
                return response
            else:
                print("Incorrect choice\n")
        
    def display_list_results(self, results):
        """
        Displays the results from a list one result per line
        results: list[str]
        """
        for result in results:
            print(result)
        input("\npress <enter> to continue\n")
        
    def get_value(self, prompt):
        """
        Displays prompt and returns user response
        
        prompt: str
        return: str
        """
        
        print(prompt)
        return input("> ")    
    
    def display_member_details(self,member):
        """
        Displays the member name, address and amount owing
        
        member: (str,str,float)
        """
        
        print(f"{member[0]}\t{member[1]}\t{member[2]}")
        
        input("\npress <enter> to continue\n")
    
    def display_movie_details(self, movies):
        """
        Dispalys the movie details

        movies: list
        """

        for movie in movies:
            print(f"{movie[0]} ({movie[2]}) directed by {movie[3]}. Run time {movie[1]}")
        
        input("\npress <enter> to continue\n")

    def display_movies_on_loan(self,movies):
        """
        Displays the movies that are one loan
        
        movies: list[(str,str,str)]
        """
        
        for movie in movies:
            print(f"{movie[0]} on loan to {movie[1]}. Due back on {movie[2]}")
            
        input("\npress <enter> to continue\n")

    def input_member_details(self):
        """
        User inputs member details

        return: ("str", "str")
        """

        last_name = self.get_value("Enter member's last name")
        initial = self.get_value("Enter member's initial")
        address = self.get_value("Enter member's address")

        name = last_name + "," + initial

        return(name, address)

    def operation_results(self,result):
        """
        Displays the success of the operation
        
        results: (bool,str)
        """
        
        if result[0] == True:
            print(f"Success: {result[1]}")
        else:
            print(f"Error: {result[1]}")
            
        input("\npress <enter> to continue\n")