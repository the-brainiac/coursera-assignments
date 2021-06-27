#!/usr/bin/env python3

import emails
import os
import reports

table_data=[
  ['Name', 'Amount', 'Value'],
  ['elderberries', 10, 0.45],
  ['figs', 5, 3],
  ['apples', 4, 2.75],
  ['durians', 1, 25],
  ['bananas', 5, 1.99],
  ['cherries', 23, 5.80],
  ['grapes', 13, 2.48],
  ['kiwi', 4, 0.49],
]
reports.generate("/tmp/report.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)
table_data = cars_dict_to_table(data)
reports.generate("/tmp/cars.pdf", summary, "This is cars list.", table_data)

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "List of Fruits"
body = "Hi\n\nI'm sending an attachment with all my fruit."

message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")
emails.send(message)


sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Sales summary for last month"
body = "The same summary from the PDF, but using \n between the lines"

message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
emails.send(message)
