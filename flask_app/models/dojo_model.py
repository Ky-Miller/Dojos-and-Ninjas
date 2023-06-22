from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model
# Have import from mysqlconnection on every model for DB interactions
# Import the model's python file as a module, not the class directly so you avoid circular import errors!
# For example: from flask_app.models import table2_model

'''
! Note: If you are working with tables that are related to each other, 
!       you'll want to import the other table's class here for when you need to create objects with that class. 

! Example: importing pets so we can make pet objects for our users that own them.

Class should match the data table exactly that's in your DB.

REMEMBER TO PARSE DATA INTO OBJECTS BEFORE SENDING TO PAGES!

'''
class Dojo:
    DB= "dojos_and_ninjas"

    def __init__(self, data) -> None:
        self.dojo_id    = data[    "ID"    ]
        self.name       = data[   "name"   ]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = """
        SELECT *
        FROM dojos;
        """

        results = connectToMySQL(cls.DB).query_db(query)

        all_dojos = []

        for dojo in results:

            all_dojos.append(cls(dojo))
        
        return all_dojos

    @classmethod
    def add_dojo( cls , data ):

        query = """
        INSERT INTO dojos ( name )
        VALUES ( %(name)s );
        """

        return connectToMySQL(cls.DB).query_db( query, data)

    @classmethod
    def get_dojo(cls, data):
        query = """
        SELECT *
        FROM dojos
        WHERE dojos.ID = %(dojo_id)s;
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return cls(results[0])
    
    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = """
        SELECT * FROM dojos
        LEFT JOIN ninjas ON ninjas.dojo_ID = dojos.ID
        WHERE dojos.ID = %(dojo_id)s;
        """
        results = connectToMySQL(cls.DB).query_db( query , data )
        dojo = cls( results[0] )
        for row_from_db in results:
            print(row_from_db)
            ninja_data = {
                "ID"         : row_from_db[    "ninjas.ID"    ],
                "first_name" : row_from_db["first_name"],
                "last_name"  : row_from_db[ "last_name"],
                "age"        : row_from_db[    "age"   ],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"],
                "dojo_ID"    : row_from_db[  "dojo_ID" ]
            }
            dojo.ninjas.append(ninja_model.Ninja( ninja_data ) )
        
        return dojo