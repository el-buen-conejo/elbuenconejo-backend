from utils.states_catalog.sql_class_states import ExecuteSqlStates


def run():
    print("Initializing states catalog to purge.")
    sql_sentence = ExecuteSqlStates("STATES_TABLE", "scripts/csv_files/states_list.csv")
    print("Deleting Users table.")
    print("Load fake data into Users table.")
    sql_sentence.csv_file_name()
    print("Everything in User table was setting up")
