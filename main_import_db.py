from custom_modules.import_functions import import_brand_from_db

selected_brand = input("Voer merk in:\n").upper()

df_cars_imported = import_brand_from_db(selected_brand)

print(df_cars_imported)
