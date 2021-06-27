"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import pygal

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
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

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
# print(read_csv_as_nested_dict('isp_gdp.csv', 'Country Name', ',', '"')['Aruba'])
def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output: 
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    res = []
    for key in gdpdata:
        try:
            year = int(key)
            if gdpdata[key] and gdpinfo['min_year'] <= year and year <= gdpinfo['max_year']:
                res.append((year, float(gdpdata[key])))
        except ValueError:
            pass
    return res

def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values 
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """
    nested_dict = read_csv_as_nested_dict(gdpinfo['gdpfile'], 
                                          gdpinfo['country_name'], 
                                          gdpinfo['separator'], 
                                          gdpinfo['quote'])
    country_dict = dict()
    for country in country_list:
        if country not in nested_dict:
            country_dict[country] = []
            continue
        temp_dict = {}
        min_year = gdpinfo['min_year']
        max_year = gdpinfo['max_year']
        for year in range(min_year, max_year+1):
            temp_dict[str(year)] = nested_dict[country][str(year)]
        # print(temp_dict)
        country_dict[country] = build_plot_values(gdpinfo, temp_dict)
    # print(country_dict)
    return country_dict

def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """
    data = build_plot_dict(gdpinfo, country_list)
    xyplot = pygal.XY(heihgt=500)
    xyplot.title = 'GDP Data of Countries'
    for country in data:
      coord = data[country]
      xyplot.add(country, coord)
    xyplot.render_to_file(plot_file)

    return


def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    render_xy_plot(gdpinfo, [], "isp_gdp_xy_none.svg")
    render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    render_xy_plot(gdpinfo, ["United Kingdom", "United States"],
                   "isp_gdp_xy_uk+usa.svg")
    render_xy_plot(gdpinfo, ["India", "China", "United Kingdom", "United States", "Aruba", "Andorra", "Angola", "Afghanistan", "Albania"], "isp_gdp_xy_countries.svg")


# Make sure the following call to test_render_xy_plot is commented out
# when submitting to OwlTest/CourseraTest.

test_render_xy_plot()
