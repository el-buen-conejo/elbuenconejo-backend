from utils.addresses.sql_class_addresses import ExecuteSqlAddress


def run():
    print("Initializing states catalog to purge.")
    sql_sentence = ExecuteSqlAddress(
        "ADDRESSES_TABLE", "scripts/csv_files/addresses.csv"
    )
    print("Deleting  Addresses table.")
    print("Load fake data into Addresses table.")
    sql_sentence.csv_file_name()
    print("Everything in Addresses table was setting up")
