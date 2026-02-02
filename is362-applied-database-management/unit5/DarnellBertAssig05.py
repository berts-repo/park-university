"""
DarnellBertAssig05.py
Bert Darnell
IS3362 - John Ciarrochi
Unit 5 - Assignment 5

This script creates two tables, assig05.Client and assig05.Contract, and populates them with the records provided in the instructions, then it creates a relation between Contract.ClientID and Client.ClientID
"""


import mariadb

userAux = input("Enter user: ")
passwordAux = input("Enter password: ")

conn = mariadb.connect(
    user=userAux,
    password=passwordAux,
    host="localhost",
    database="assig05"
)
cur = conn.cursor()

# Creates Client table with attributes
createClientTable = """
CREATE TABLE Client (
    ClientID VARCHAR(7),
    Name TEXT,
    LegalAddress TEXT,
    Phone TEXT,
    PRIMARY KEY (ClientID)
    )
"""

# Creates Contract table with attributes
createContractTable = """
CREATE TABLE Contract (
    ContractNo VARCHAR(7) PRIMARY KEY,
    ClientID VARCHAR(7),
    IsLongTerm BOOLEAN
    )
"""

# Populates Client table
fillClientTable = """
INSERT INTO Client VALUES 
("933256Q", "Jerry Seinfeld", "PO Box 12221 Delaware 19702", "555-555-0001"),
("278544C", "Chris Rock", "PO Box 354 Delaware 19703", "555-555-0002"),
("765256P", "Eddie Murphee", "PO Box 4287 Delaware 19703", "555-555-0003"),
("736533Q", "Jay Leno", "PO Box 216 Delaware 19702", "555-555-0004"),
("865263C", "Wanda Sykes", "PO Box 56944 Delaware 19706", "555-555-0005"),
("842471P", "Whopie Goldberg", "PO Box 884 Delaware 19706", "555-555-0006"),
("156836P", "Joy Behar", "PO Box 687 Delaware 19706", "555-555-0007"),
("145696S", "Sarah Silverston", "PO Box 4622 Delaware 19707", "555-555-0008"),
("394204C", "Conan Brian", "PO Box 34344 Delaware 19707", "555-555-0009"),
("472507P", "Charles Chaplin", "PO Box 9587 Delaware 19707", "555-555-0010")
"""

# Populates Contract Table
fillContractTable = """
INSERT INTO Contract VALUES 
("CO0011", "278544C", TRUE),
("CO0013", "736533Q", TRUE),
("CO0014", "865263C", TRUE),
("CO0016", "156836P", TRUE),
("CO0018", "394204C", TRUE),
("CO0010", "933256Q", FALSE),
("CO0012", "765256P", FALSE),
("CO0015", "842471P", FALSE),
("CO0017", "145696S", FALSE),
("CO0019", "472507P", FALSE)
"""

# Creates FK relation
alterTableContract = """
alter table Contract
ADD CONSTRAINT FK_Contract_to_Client
FOREIGN KEY (ClientID) REFERENCES Client(ClientID)
ON DELETE RESTRICT
"""

# Run SQL statements
try:
    cur.execute(createClientTable)
    cur.execute(createContractTable)
    cur.execute(fillClientTable)
    cur.execute(fillContractTable)
    cur.execute(alterTableContract)
except mariadb.Error as e:
    print(f"Error: {e}")

conn.commit()
conn.close()


