"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
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

def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    countries = gdp_countries.keys()
    # print(countries)
    country_dict = dict()
    country_set = set()
    for code in plot_countries:
        if plot_countries[code] in countries:
            country_dict[code] = plot_countries[code]
        else:
            country_set.add(code)
    return country_dict, country_set

def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    nested_dict = read_csv_as_nested_dict(gdpinfo['gdpfile'], 
                                          gdpinfo['country_name'], 
                                          gdpinfo['separator'], 
                                          gdpinfo['quote'])
    # print(nested_dict)
    gdp_dict = dict()
    set2 = set()
    for country in nested_dict:
        gdp = nested_dict[country][year]
        country_code = ''
        for code in plot_countries:
            if plot_countries[code] == country:
                country_code = code
                break
        if gdp and country_code:
            gdp_dict[country_code] = math.log(float(gdp), 10)
        if not gdp:
            set2.add(country_code)
    # print(gdp_dict)
    set1 = set()
    countries = nested_dict.keys()
    for code in plot_countries:
        if plot_countries[code] not in countries:
            set1.add(code)
    # print(set1)
    return gdp_dict, set1, set2


def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    data = build_map_dict_by_name(gdpinfo, plot_countries, year)
    # print(data[0])
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'GDP data for year {}'.format(year)
    worldmap_chart.add("GDP for {}".format(year), data[0])
    worldmap_chart.add("Missing From world bank data", data[1])
    worldmap_chart.add("No GDP data", data[2])
    worldmap_chart.render_to_file(map_file)
    return


def test_render_world_map():
    """
    Test the project code for several years.
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

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

test_render_world_map()
