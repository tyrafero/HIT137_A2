def csv_to_txt():
    with open('csv/CSV1.csv', 'r') as file:
        data = file.read().split('\n')

    output_text = ""
    for x in range(1, len(data)):
        row = data[x].split(',')
        if len(row) >= 3:
            output_text += row[2] + "\n"
        else:
            print(f"Row {x} does not have enough columns.")

    with open('output/output.txt', 'w') as output_file:
        output_file.write(output_text)

csv_to_txt()