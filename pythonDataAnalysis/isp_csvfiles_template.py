"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    field_names = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            field_names.append(row)
            break
    # print(field_names[0])
    return field_names[0]

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    field_names = read_csv_fieldnames(filename, separator, quote)
    list_dict = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=separator, quotechar=quote)
        for row in list(csvreader)[1:]:
            field_dict = dict()
            for field in range(len(field_names)):
                field_dict[field_names[field]] = row[field]
            list_dict.append(field_dict)
    # print(field_names)
    return list_dict


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    list_dict = read_csv_as_list_dict(filename, separator, quote)
    fields = []
    for field in list_dict:
        fields.append(field[keyfield])
    re_dict = dict()
    for field in range(len(list_dict)):
        re_dict[fields[field]] = list_dict[field]

    return re_dict


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=separator, quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow(fieldnames)
        for data in table:
            fields = []
            for field in fieldnames:
                fields.append(data[field])
            csv_writer.writerow(fields)
# write_csv_from_list_dict('output1.csv', [{'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14}, {'a': 20, 'b': 21, 'c': 22, 'd': 23, 'e': 24}, {'a': 30, 'b': 31, 'c': 32, 'd': 33, 'e': 34}, {'a': 40, 'b': 41, 'c': 42, 'd': 43, 'e': 44}], ['a', 'b', 'c', 'd', 'e'], ',', '"')