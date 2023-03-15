# Paso 1: Crea una funcion para poder leer el archivo status.txt y generar una lista con los datos
def read_file():
    data = set()
    with open('status.txt', 'r') as f:
        for line in f.readlines():
            data.add(line.strip())
    return data

# Paso 2: Crea otra function para normalizar los datos de la lista
def clean_data(data_file):
    clean_data = []
    for data in data_file:
        line = data.replace(',', '')
        line = data.replace('?', '')
        line = data.replace('¿', '')
        line = data.replace('¡', '')
        line = data.replace('!', '')
        line = data.replace('.', '')
        clean_data.append(line)
    return clean_data

def normalize_data(data_file):
    data_normalize = []
    for data in data_file:
        data_normalize.append(data.lower())
    return data_normalize

# Paso 3: Crea otra function para identificar si las rutas estan abiertas o cerradas
def identify_data(data_file):
    data_identify = []
    for data in data_file:
        if "todas las rutas están abiertas" in data:
            data_identify.append([data, 1, 1])
        elif "todas las rutas están cerradas" in data:
            data_identify.append([data, 0, 0])
        elif "valenciana está abierta" in data:
            data_identify.append([data, 1, 0])
        elif "borja está cerrada" in data:
            data_identify.append([data, 0, 1])
    return data_identify

# Paso 4: Crea otra function para generar el archivo csv con los datos normalizados
def main():
    """
    La funcion main es la funcion principal del programa
    """
    data = read_file()
    data = clean_data(data)
    data = normalize_data(data)
    
    with open('status.csv', 'w') as f:
        import csv
        headers = ['status', 'valenciana', 'borja']
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(identify_data(data))


# Ejecuta la funcion main
if __name__ == '__main__':
    main()