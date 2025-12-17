from sqlalchemy import create_engine, text
db_connection_string = "postgresql://postgres:1957411@localhost:5432/QA"
db = create_engine(db_connection_string)

def test_select():
    connection = db.connect()
    connection.begin()
    result = connection.execute(text("SELECT * FROM student"))
    rows = result.mappings().all()
    row17 = rows[16]

    assert row17["user_id"] == 3865
    assert row17["education_form"] == "personal"
    connection.close()

def test_select_1row_with_two_filters():
    connection = db.connect()
    sql = text("SELECT FROM student WHERE \"level\" = :level AND \"education_form\" = :education_form")
    result = connection.execute(sql, {"level": "Advanced", "education_form": "personal"})
    rows = result.mappings().all()

    assert len(rows) == 4

def test_add_new():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("INSERT INTO student (\"user_id\", \"level\", \"education_form\", \"subject_id\") VALUES (:user_id, :level, :education_form, :subject_id)")
    params = {
        "user_id": 12,
        "level": "Advanced",
        "education_form": "personal",
        "subject_id": 1
        }
    connection.execute(sql, params)
    transaction.commit()
    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("UPDATE student SET education_form = :personal WHERE user_id = :id")
    connection.execute(sql, {"personal":"group", "id": 12})
    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("DELETE FROM student WHERE user_id = :id")
    connection.execute(sql, {"id": 12})
    transaction.commit()
    connection.close()