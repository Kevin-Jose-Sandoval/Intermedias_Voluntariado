import pandas as pd

# file details 
file_path = ".\input.xlsx"
# 3 = Customer type | 4 = Gender |  5 = Product line | 6 = Unit price | 7 = Quantity | 12 = Payment
columns_to_read = [3, 4, 5, 6, 7, 12]


def read_file():
    print("Leyendo archivo...")

    # read excel
    data_frame = pd.read_excel(file_path, 
                                sheet_name = "data", 
                                header = 0, 
                                usecols = columns_to_read 
                                )

    return data_frame


def add_filters(data_frame):
    print("Agregando filtros")

    # apply filter
    data_frame = data_frame[data_frame["Payment"] == "Cash"]

    return data_frame


def main():
    try:
        data_frame = read_file()
        data_frame = add_filters(data_frame)

        # export the new excel with filter
        data_frame.to_excel("./output.xlsx", sheet_name = "output", index = False)
        print("Proceso terminado")

    except:
        print("Ocurrió un error en el proceso")


if __name__ == '__main__':
    main()