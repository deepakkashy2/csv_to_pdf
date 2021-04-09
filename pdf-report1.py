from __future__ import print_function
import pandas
import os

import numpy as np


df=pandas.read_csv("dd.csv")

print(type(df))
print(df)
sales_report = df
sales_report.head()

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")

template_vars = {"title" : "Sales Funnel Report - National",
                 "national_pivot_table": sales_report.to_html()}

html_out = template.render(template_vars)
from weasyprint import HTML
HTML(string=html_out).write_pdf("report.pdf")