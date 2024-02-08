from utils.cities_catalog.sql_class_cities import ExecuteSqlCities


def run():
    print("Initializing states catalog to purge.")
    sql_sentence = ExecuteSqlCities("CITIES_TABLE", "scripts/csv_files/cities_list.csv")
    print("Deleting  Cities table.")
    print("Load fake data into Cities table.")
    sql_sentence.csv_file_name()
    print("Everything in Cities table was setting up")
