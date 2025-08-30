from sqlalchemy import create_engine, text

class bd_arguments:
    def __init__(self, connection_string):
        self._db = create_engine(connection_string)

    def create_sub(self, id, title):
        with self._db.connect() as conn:
            sql = text("INSERT INTO subject (subject_id, subject_title) VALUES (:new_id, :new_title) RETURNING *")
            result = conn.execute(sql, {"new_id": id, "new_title": title})
            row = result.mappings().first()  
            return row

    def delete_sub(self, id):
        with self._db.connect() as conn:
            sql = text("DELETE FROM subject WHERE subject_id = :test_id")
            conn.execute(sql, {"test_id": id})

    def sub_list(self, id):
        with self._db.connect() as conn:
            sql = text("SELECT * FROM subject WHERE subject_id = :test_id")
            result = conn.execute(sql, {"test_id": id})
            rows = result.mappings().all()
            return rows

    def change(self, params, id):
        with self._db.connect() as conn:
            sql = text("UPDATE subject SET subject_title = :changed_text WHERE subject_id = :test_id RETURNING *")
            result = conn.execute(sql, {"changed_text": params, "test_id": id})
            row = result.mappings().first() 
            return row