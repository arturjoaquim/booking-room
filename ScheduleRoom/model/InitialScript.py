from ConnectionFactory import ConnectionFactory

connection = ConnectionFactory.create_connection()

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS cadroom ')
cursor.execute('''CREATE TABLE "cadroom" (
	"id_room"	INTEGER,
	"nm_room"	TEXT NOT NULL UNIQUE,
	"nm_addr"	TEXT NOT NULL,
	"nm_desc"	TEXT NOT NULL,
	"dt_cad"	TEXT NOT NULL,
	PRIMARY KEY("id_room")
)''')


cursor.execute('DROP TABLE IF EXISTS cadusr')
cursor.execute('''CREATE TABLE "cadusr" (
	"id_usr"	INTEGER,
	"nm_usr"	TEXT NOT NULL UNIQUE,
	"key_usr"	TEXT NOT NULL,
	"dt_cad"	TEXT NOT NULL,
	PRIMARY KEY("id_usr")
)
''')

cursor.execute('DROP TABLE IF EXISTS rqst_bkng')
cursor.execute('''CREATE TABLE "rqst_bkng" (
	"id_bkng"	INTEGER,
	"nm_bkng"	TEXT NOT NULL,
	"id_room"	INTEGER NOT NULL,
	"id_bkng_user"	INTEGER NOT NULL,
	"nm_desc"	TEXT,
	"dt_bkng"	TEXT NOT NULL,
    "nm_prdo"   TEXT NOT NULL,
	"dt_cad"	TEXT NOT NULL,
	FOREIGN KEY("id_room") REFERENCES "cadroom"("id_room"),
	FOREIGN KEY("id_bkng_user") REFERENCES "cadusr"("id_usr"),
	PRIMARY KEY("id_bkng")
)
''')


cursor.execute('''INSERT INTO cadroom VALUES(1, "Laboratório V", "3 andar, Prédio Principal", "Laboratório de Informática, com 60 computadores.", "2024-06-12"),
               (2, "Laboratório IV", "3 andar, Prédio Principal", "Laboratório de Informática, com 60 computadores.", "2024-06-12"),
               (3, "Laboratório III", "3 andar, Prédio Principal", "Laboratório de Informática, com 60 computadores.", "2024-06-12"),
               (4, "Laboratório II", "3 andar, Prédio Principal", "Laboratório de Informática, com 60 computadores.", "2024-06-12")
''')

cursor.execute('INSERT INTO cadusr VALUES (1, "artur", "123", "2024-06-12")')
cursor.execute('''INSERT INTO rqst_bkng VALUES (1, "Aula de Python", 1, 1, "Aula para introduzir python aos alunos do 3 semestre de ADS.", "2024-06-26", "Noite", "2024-06-12"),
               (2, "Aula de Python", 1, 1, "Aula para introduzir python aos alunos do 3 semestre de ADS.", "2024-06-26", "Manhã", "2024-06-12"),
               (3, "Aula de Python", 1, 1, "Aula para introduzir python aos alunos do 3 semestre de ADS.", "2024-06-25", "Manhã", "2024-06-12"),
               (4, "Aula de Python", 1, 1, "Aula para introduzir python aos alunos do 3 semestre de ADS.", "2024-06-24", "Manhã", "2024-06-12"),
               (5, "Aula de Python", 1, 1, "Aula para introduzir python aos alunos do 3 semestre de ADS.", "2024-06-25", "Noite", "2024-06-12"),
               (6, "Aula de Python", 1, 1, "Aula para introduzir python aos alunos do 3 semestre de ADS.", "2024-06-24", "Noite", "2024-06-12")
''')

connection.commit()
connection.close()
