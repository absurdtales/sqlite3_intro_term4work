import sqlite3
class DataStore:
    def __init__(self):
        """
        Initialise the Datastore instance
        """
        # ---- Attirbutes ---- #
        self.connection = sqlite3.connect("movies.db")
        self.cursor = self.connection.cursor()

    def __del__(self):
        """
        Write data in cache and close connection when program finishes
        """
        self.connection.commit()
        self.connection.close()

    def get_countries(self):
        
        """
        Displays the countries from director table
        
        returns: list[str]
        """
        
        self.cursor.execute(
        """
        SELECT DISTINCT country
        FROM director
        ORDER BY country ASC
        """
        )
        
        results = self.cursor.fetchall()
        
        clear_results = []
        
        for result in results:
            clear_results.append(result[0])
        
        return clear_results

    def get_members(self):
        
        """
        Displays the members from member table
        
        returns: list[str]
        """
        self.cursor.execute (
        """
        SELECT memname
        FROM members
        ORDER by memname ASC
        """
        )
        results = self.cursor.fetchall()
        clear_results = []
        for result in results:
            clear_results.append(result[0])
        return clear_results
    
    def get_movies(self):
        """
        Displays the movies from movies table
        
        returns: list[str]
        """
        self.cursor.execute (
        """
        SELECT movname
        FROM movie
        ORDER by movname ASC
        """  
        )
        results = self.cursor.fetchall()
        clear_results = []
        for result in results:
            clear_results.append(result[0])
        return clear_results

    def get_dir_by_country(self, var):
        """
        Displays the directors that are chosen from arugment and their respective country
        
        input: var[str]
        returns: list[str]
        """
        self.cursor.execute (
        """
        SELECT dirname
        FROM director
        WHERE country = :country
        """
        ,{'country': var}   
        )
        results = self.cursor.fetchall()
        clear_results = []
        for result in results:
            clear_results.append(result[0])
        return clear_results

    def get_member_details(self, member):
        """
        Displays member details based on user input
        
        input: var[str]
        returns: list[str]
        """
        self.cursor.execute(
            """
            SELECT memname, address, owes
            FROM members
            WHERE memname = :member
            """,
            {"member": member}
        )

        results = self.cursor.fetchall()
        return results[0]

    def get_member_movies(self, member):
        """
        Displays member movies on loan based on user input

        input: var[str]
        returns: list[str]
        """
        self.cursor.execute(
            """
            SELECT movname
            FROM movie
            WHERE movienumb IN(
                SELECT movienumber
                FROM movies_onhire
                WHERE memberid IN(
                    SELECT memberid
                    FROM members
                    WHERE memname = :member
                )
            )
            """,
            {"member" : member}
        )
        results = self.cursor.fetchall()

        clear_results = []

        for result in results:
            clear_results.append(result[0])

        return clear_results

    def get_director_movies(self, director):
        """
        Displays a directors movie catalogue based on user input

        input: var[str]
        returns: list[str]
        """
        self.cursor.execute(
            """
            SELECT movname
            FROM movie
            WHERE dirnumb IN(
                SELECT dirnumb
                FROM director
                WHERE dirname = :director
            )
            """,
            {"director" : director}
        )
        results = self.cursor.fetchall()

        clear_results = []

        for result in results:
            clear_results.append(result[0])
        
        return clear_results
    
    def get_movie_details(self):
        """
        Returns all movie details based on user input

        input: var[str]
        returns: list[(str, int, int, str)]
        """
        self.cursor.execute(
            """
            SELECT m.movname, m.length, m.year, d.dirname
            FROM movie AS m
            JOIN director AS d
            ON m.dirnumb = d.dirnumb
            """
        )
        results = self.cursor.fetchall()

        return results

    def get_loan_details(self):
        """
        Returns loan details based on user input

        returns: list[(str, str, str)]
        """
        self.cursor.execute(
            """
            SELECT mov.movname, mem.memname, hire.duedate
            FROM movie as mov
            JOIN movies_onhire AS hire
            ON mov.movienumb = hire.movienumber
            JOIN members as mem
            ON mem.memberid = hire.memberid
            """
        )

        results = self.cursor.fetchall()

        return results

    def add_new_member(self, name, address):
        """
        Adds new member details based on user input

        name: str
        address: str
        """

        # find new member id
        self.cursor.execute(
            """
            SELECT MAX(memberid)
            FROM members
            """
        )

        member_id = self.cursor.fetchone()[0] + 1

        # add details to database
        self.cursor.execute(
            """
            INSERT INTO members
            VALUES (:memberid, :name, :address, :owes)
            """,
            {
                "memberid": member_id,
                "name": name,
                "address": address,
                "owes": None
            }
        )

        return f"Member {name} added"
    
    def add_new_movie(self,movname,length,year,director):
        """
        Adds new movie to database, returns success
        
        movname: str
        length: int
        year: int
        director: str
        
        return: (bool,str)
        """
        
        # get director num
        self.cursor.execute(
            """
            SELECT dirnumb
            FROM director
            WHERE dirname = :director
            """,
            {"director": director}
        )
        results = self.cursor.fetchone()
        if results == None:
            return(False, f"director '{director}' does not exist")
        else:
            dirnumb = results[0]
        
        # calculate next movienumb
        self.cursor.execute(
            """
            SELECT MAX(movienumb)
            FROM movie
            """
        )
        movienumb = self.cursor.fetchone()[0]+1
        
        # write information to database
        self.cursor.execute(
            """
            INSERT INTO movie
            VALUES (:movienumb,:movname,:length,:year,:dirnumb)
            """,
            {
                "movienumb": movienumb,
                "movname": movname,
                "length": length,
                "year": year,
                "dirnumb": dirnumb
            }
        )
        return(True,f"movie '{movname}' added")
    
    def add_new_director(self,name,country):
        """
        Adds new director, returns success
        
        name: str
        country: str
        
        return: (bool,str)
        """
        
        # calcuate dirnumb
        self.cursor.execute(
            """
            SELECT MAX(dirnumb)
            FROM director
            """
        )
        dirnumb = self.cursor.fetchone()[0] + 1
    
        # add director to datasource
        self.cursor.execute(
            """
            INSERT INTO director
            VALUES (:dirnumb,:dirname,:country)
            """,
            {
                "dirnumb":dirnumb,
                "dirname":name,
                "country":country
            }
        )
        
        return (True,f"{name} added.")
    
    def add_new_loan(self,movie,member):
        """
        Adds a new movie loan to the database, returns success
        
        movie: str
        member: str
        
        return: (bool,str)
        """
        
        # check movie name
        self.cursor.execute(
            """
            SELECT movienumb
            FROM movie
            WHERE movname = :movie
            """,
            {"movie":movie}
        )
        result = self.cursor.fetchone()
        if result == None:
            return (False,f"'{movie}' is not in library")
        else:
            movienumb = result[0]
        
        # check member number
        self.cursor.execute(
            """
            SELECT memberid
            FROM members
            WHERE memname = :member
            """,
            {"member": member}
        )
        result = self.cursor.fetchone()
        if result == None:
            return (False, f"'{member}' is not a member")
        else:
            memberid = result[0]
        
        # get date and prepare due date
        duedate = cal_due_date()
        
        # add record to database
        self.cursor.execute(
            """
            INSERT INTO movies_onhire
            VALUES (:movienumb,:memberid,:duedate)
            """,
            {
                "movienumb": movienumb,
                "memberid": memberid,
                "duedate": duedate
            }
        )
        
        return (True, f"'{movie}' loaned to {member}")
    
    def return_movie(self,movie):
        """
        Removes movie from movies_on_loan table
        
        movie: str
        
        return: (bool, str)
        """
        
        # get movie number
        self.cursor.execute(
            """
            SELECT movienumber
            FROM movies_onhire
            WHERE movienumber IN (
                SELECT movienumb
                FROM movie
                WHERE movname = :movie
            )
            """,
            {"movie": movie}
        )
        result = self.cursor.fetchone()
        
        if result == None:
            return(False, f"'{movie}' is not on loan")
        else:
            movienumb = result[0]
            self.cursor.execute(
                """
                DELETE FROM movies_onhire
                WHERE movienumber = :movienumb
                """,
                {"movienumb": movienumb}
            )
            return(True, f"'{movie}' returned")

    def get_amount_owing(self,member):
        """
        Returns how much the member owes
        
        member: str
        
        returns: (bool, str)
        """
        
        self.cursor.execute(
            """
            SELECT memberid
            FROM members
            WHERE memname = :member
            """,
            {"member":member}
        )
        
        if self.cursor.fetchone == None:
            return(False,f"'{member}' not in database")
        else:
            self.cursor.execute(
                """
                SELECT owes
                FROM members
                WHERE memname = :member
                """,
                {"member":member}
            )
            
            result = self.cursor.fetchone()
            if result == None:
                return(True,0)
            else:
                return(True,result[0])
            
    def update_amount_owing(self,member, new_debt):
        """
        Reduces member's debt by payment amount
        
        memebr: str
        payment: float
        """
        
        self.cursor.execute(
            """
            UPDATE members
            SET owes = :new_debt
            WHERE memname = :member
            """,
            {
                "new_debt": new_debt,
                "member": member
            }
        )
        
        return(True,f"{member} now owes ${new_debt}")