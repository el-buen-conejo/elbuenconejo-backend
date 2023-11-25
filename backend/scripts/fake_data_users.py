from utils.users.sql_class_users import ExecuteSqlSentence


def run():
    print("Initializing database purge.")
    sql_sentence = ExecuteSqlSentence("USER_TABLE")
    print("Deleting Users table.")
    sql_sentence.reset_auto_increment_users()
    print("Load fake data into Users table.")
    sql_sentence.csv_file_name("scripts/csv_files/users.csv")
    print("Everything in User table was setting up")
