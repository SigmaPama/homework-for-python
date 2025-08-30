from ClassForTest import bd_arguments

db_connection_string = "postgresql://postgres:255@localhost:5432/subject"
api = bd_arguments(db_connection_string)

def test_create_subject():
    create = api.create_sub(18, "Test")
    assert create['subject_id'] == 18
    assert create['subject_title'] == "Test"
    api.delete_sub(create['subject_id'])

def test_change_sub():
    create = api.create_sub(20, "test")
    change_text = api.change("test_pass", 20)
    assert create["subject_id"] == change_text["subject_id"]
    api.delete_sub(change_text["subject_id"])

def test_delete_subject():
    create = api.create_sub(30, "Test")
    list_before = api.sub_list(30)
    assert create["subject_id"] == list_before[0]["subject_id"]
    api.delete_sub(30)
    list_after = api.sub_list(30)
    assert len(list_before) == 1 
    assert len(list_after) == 0   