from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB= "dojos_and_ninjas"

    def __init__(self, data) -> None:
        self.id         = data[     "ID"     ]
        self.first_name = data[ "first_name" ]
        self.last_name  = data[ "last_name"  ]
        self.age        = data[    "age"     ]
        self.created_at = data[ "created_at" ]
        self.updated_at = data[ "updated_at" ]
        self.dojo_id    = data[  "dojo_ID"   ]

    @classmethod
    def get_all_ninjas(cls):
        query = """
        SELECT *
        FROM ninjas;
        """

        results = connectToMySQL(cls.DB).query_db(query)

        all_ninjas = []

        for ninja in results:

            all_ninjas.append(cls(ninja))

    @classmethod
    def add_ninja(cls, data):
        query = """
        INSERT INTO dojos_and_ninjas.ninjas (first_name, last_name, age, dojo_ID)
        VALUES(  %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s  );
        """

        return connectToMySQL(cls.DB).query_db(query, data)      
