# family dictionary, main data structure holding all the family memebrs as an individual objects.
class Person:
    # Create class called Person to store individual family members with their attributes
    def __init__(self, name, birthdate, deathdate, parent1, parent2):
        self.name = name
        self.birthdate = birthdate
        self.deathdate = deathdate
        self.parent1 = parent1
        self.parent2 = parent2



family_dict = { "Otto Emmersohn": Person("Otto Emmersohn", "1930-10-03", "null", "Karl Emmersohn", "Anna Bauer"),  # Alive
                "Karl Emmersohn": Person("Karl Emmersohn", "1900-10-03", "null", "Franz Emmersohn", "Maria Hoffmann"),  # Alive
                "Anna Bauer": Person("Anna Bauer", "1902-12-08", "null", "Wilhelm Bauer", "Elisabeth Schmitt"),  # Alive
                "Franz Emmersohn": Person("Franz Emmersohn", "1870-01-12", "1945-06-15", "Johann Emmersohn", "Greta Müller"),  # Dead
                "Maria Hoffmann": Person("Maria Hoffmann", "1875-10-07", "1950-01-25", "Heinrich Hoffmann", "Klara Steiner"),  # Dead
                "Wilhelm Bauer": Person("Wilhelm Bauer", "1878-05-05", "1955-10-30", "Max Bauer", "Friedrike Weber"),  # Dead
                "Elisabeth Schmitt": Person("Elisabeth Schmitt", "1880-07-01", "1965-03-09", "Richard Schmitt", "Emilie Ziegler"),# Dead
                "Hans Emmersohn": Person("Hans Emmersohn", "1932-02-08", "null", "Karl Emmersohn", "Anna Bauer"),  # Alive
                "Greta Emmersohn": Person("Greta Emmersohn", "1935-03-05", "null", "Karl Emmersohn", "Anna Bauer"),  # Alive
                "Lukas Emmersohn": Person("Lukas Emmersohn", "1938-01-10", "null", "Karl Emmersohn", "Anna Bauer"),  # Alive
                "Liselotte Bauer": Person("Liselotte Bauer", "1931-04-12", "null", "Wilhelm Bauer", "Elisabeth Schmitt"),  # Alive
                "Friedrich Hoffmann": Person("Friedrich Hoffmann", "1929-10-10", "null", "Heinrich Hoffmann", "Klara Steiner"),# Alive
                "Helga Müller": Person("Helga Müller", "1933-06-11", "2011-08-05", "Rudolf Müller", "Sophie Becker"),  # Dead
                "Laura Emmersohn": Person("Laura Emmersohn", "1890-03-12", "1970-09-10", "Franz Emmersohn", "Maria Hoffmann"),  # Dead
                "Kevin Emmersohn": Person("Kevin Emmersohn", "1890-05-12", "1970-09-10", "Franz Emmersohn", "Maria Hoffmann"),  # Dead
                "David Smith": Person("David Smith", "1890-05-12", "1970-09-10", "Lucas Smith", "Laura Emmersohn"),  # Dead
                "Anthony Emmersohn": Person("Anthony Emmersohn", "1890-12-12", "1970-09-10", "Kevin Emmersohn", "Lucy Flower"),# Dead
                "Cornelia Emmersohn": Person("Cornelia Emmersohn", "1978-10-01", "null", "Edna Emmersohn", "Harold Emmersohn"),# Alive
                "Edna Emmersohn": Person("Edna Emmersohn", "1948-07-28", "null", "Margaret Emmersohn", "John Emmersohn"),  # Alive
                "Harold Emmersohn": Person("Harold Emmersohn", "1942-01-10", "null", "Angela Smith", "Steven Emmersohn"),  # Alive
                "Emily Emmersohn": Person("Emily Emmersohn", "1984-05-10", "null", "Edna Emmersohn", "Harold Emmersohn"),  # Alive
                "Oliver Emmersohn": Person("Oliver Emmersohn", "1980-06-11", "null", "Edna Emmersohn", "Harold Emmersohn"),  # Alive
                "Margaret Emmersohn": Person("Margaret Emmersohn", "1925-01-17", "1985-10-31", "Edith Emmersohn", "Dave Emmersohn"),# Dead
                "Frank Emmersohn": Person("Frank Emmersohn", "1958-04-04", "null", "Margaret Emmersohn", "John Emmersohn"),  # Alive
                "Clara Emmersohn": Person("Clara Emmersohn", "1954-05-23", "null", "Margaret Emmersohn", "John Emmersohn"),  # Alive
                "John Emmersohn": Person("John Emmersohn", "1924-12-07", "1994-07-30", "Edna Emmersohn", "Harold Emmersohn"),  # Dead
                "Dave Emmersohn": Person("Dave Emmersohn", "1884-05-26", "1947-01-12", "Agatha Emmersohn", "Gerald Emmersohn"),# Dead
                "Gavin Emmersohn": Person("Gavin Emmersohn", "1946-06-18", "null", "Angela Smith", "Steven Emmersohn"),  # Alive
                "Reece Emmersohn": Person("Reece Emmersohn", "1988-03-04", "null", "Amanda Davis", "Frank Emmersohn"),  # Alive
                }