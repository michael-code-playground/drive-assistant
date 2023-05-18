from pydrive2.drive import GoogleDrive
from pydrive2.auth import GoogleAuth
from datetime import datetime
import csv
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)

date_time_created = datetime.now()
default_document_name = date_time_created.date().strftime("%d.%m")

#find all files containing 'template' with limited visibility to filter out results
file_list = drive.ListFile({'q':"fullText contains 'Template' and visibility = 'limited'"}).GetList()

#determine id of the folder where templates will be moved (the one named 'TEMPLATES')
for file1 in file_list:
  if file1['title']=="TEMPLATES":
    folder_for_templates_id = file1['id']  
for file1 in file_list:
  
  #print available templates
  print('title: %s, id: %s, mimeType: %s' % (file1['title'], file1['id'], file1['mimeType']))
  if file1['title']=="TEMPLATES":
    continue  
  
  #move templates to the folder
  file2 = drive.CreateFile({'id':file1['id']})
  file2.Upload()
  file2['parents'] = [{"kind": "drive#parentReference", "id": folder_for_templates_id}]
  file2.Upload()

#open the file defining where each template should be copied
try:
  with open('assignments.csv', 'r', newline='') as assignments:
    reader = csv.reader(assignments, delimiter=';',quotechar='"')
    for row in reader:
      if row[0] == 'FILE_ID':
        continue 
      file_id = row[0]
      target_folder_id = row[1]
      file_to_copy = drive.CreateFile({'id': file_id})
      file_to_copy.Copy({'id': target_folder_id}, default_document_name)
except EnvironmentError:
  print("File not found")

