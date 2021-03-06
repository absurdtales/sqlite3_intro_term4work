from datastore import DataStore
from interface import UI
from titlewindow import TitleWindow
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
db = DataStore()
ui = TitleWindow()
running = True

while running:
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main_win = TitleWindow()
        main_win.show()
        sys.exit(app.exec())
    # 1 Queries
    '''
    if option == "1":
        queries = True
        while queries:
            query = ui.query_menu()

            # Different queries inside the menu
            if query == "1":
                ui.display_list_results(db.get_countries())
            
            elif query == "2":
                ui.display_list_results(db.get_members())

            elif query == "3":
                ui.display_list_results(db.get_movies())
            
            elif query == "4":
                country = ui.get_value("Enter Country: ")
                ui.display_list_results(db.get_dir_by_country(country))
            
            elif query == "5":
                member = ui.get_value("Enter member name: ")
                ui.display_member_details(db.get_member_details(member))
            
            elif query == "6":
                member = ui.get_value("Enter member name: ")
                ui.display_list_results(db.get_member_movies(member))
            
            elif query == "7":
                director = ui.get_value("Enter director name: ")
                ui.display_list_results(db.get_director_movies(director))

            elif query == "8":
                ui.display_movie_details(db.get_movie_details())

            elif query == "9":
                ui.display_movies_on_loan(db.get_loan_details())
            
            elif query == "Q":
                print("\n")
                queries = False

    # 2 Update
    if option == "2":
        updates = True
        while updates:
            update = ui.update_menu()

            # Different queries inside the menu
            if update == "1":
                mem_name, mem_address = ui.input_member_details()
                ui.operation_results(db.add_new_member(mem_name, mem_address))

            elif update == "Q":
                print("\n")
                updates = False
    '''
    def signals(self):
        self.ui.query_menu_button.clicked.connect()
        self.ui.update_database_menu_button.clicked.connect()
        self.ui.exit_button.clicked.connect(self.exit())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = TitleWindow()
    main_win.show()
    sys.exit(app.exec())


            