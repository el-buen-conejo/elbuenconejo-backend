from utils.profiles.sql_class_profiles import ExecuteSqlProfile


def run():
    print("Initializing Profiles table to purge.")
    sql_sentence = ExecuteSqlProfile("PROFILES_TABLE", "scripts/csv_files/profiles.csv")
    print("Deleting  Profiles table.")
    print("Load fake data into Profiles table.")
    sql_sentence.csv_file_name()
    print("Everything in Profiles table was setting up")
