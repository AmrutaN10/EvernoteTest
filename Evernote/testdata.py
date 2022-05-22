import pandas as pd
import openpyxl

df = pd.read_excel('TestDataUnittest.xlsx',sheet_name='TestData')
valid_email = df.loc[0].at['Username']
valid_password = df.loc[0].at['Password']
invalid_email = df.loc[1].at['Username']
invalid_password = df.loc[1].at['Password']

df1 = pd.read_excel('TestDataUnittest.xlsx',sheet_name='url')
evernote_Url = df1.loc[0].at['URL']

df2 = pd.read_excel('TestDataUnittest.xlsx',sheet_name='Notes')
NotesTitle = df2.loc[0].at['Text']
NotesBody = df2.loc[1].at['Text']