from pydrive2.drive import GoogleDrive
from quickstart import gauth
from datetime import datetime
import csv
drive = GoogleDrive(gauth)
#file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
#file1.SetContentString('Hello World!') # Set content of the file from given string.
#file1.Upload()
date_time_created = datetime.now()
default_document_name = date_time_created.date().strftime("%d.%m")
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s, mimeType: %s' % (file1['title'], file1['id'], file1['mimeType']))



print("Content of German folder")
folder_id = '11i7u67IV4Ukzl730Go2ENPeo3T1E6XNn'
files = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
for file1 in files:
  print('title: %s, id: %s, mimeType: %s' % (file1['title'], file1['id'], file1['mimeType']))


print("test - all documents in the main folder")
files = drive.ListFile({'q': f"'root' in parents and mimeType='application/vnd.google-apps.document'"}).GetList()

for file1 in files:
  print('title: %s, id: %s' % (file1['title'], file1['id']))

print("test - display folders")
folders_on_drive = drive.ListFile({'q': f"'root' in parents and mimeType='application/vnd.google-apps.folder'"}).GetList()
for folder in folders_on_drive:

  folder_id = folder['id']
  files = drive.ListFile({'q': f"'{folder_id}' in parents and mimeType='application/vnd.google-apps.document'"}).GetList()
  for file1 in files:
    print('title: %s, id: %s' % (file1['title'], file1['id']))

print("Test if it displays all the data on google drive and content of each folder\n")
file_list = drive.ListFile({'q':"fullText contains 'Template' and visibility = 'limited'"}).GetList()
for file1 in file_list:
  if file1['title']=="TEMPLATES":
    folder_for_templates_id = file1['id']  
for file1 in file_list:
  print('title: %s, id: %s, mimeType: %s' % (file1['title'], file1['id'], file1['mimeType']))
  if file1['title']=="TEMPLATES":
    continue  
  file2 = drive.CreateFile({'id':file1['id']})
  file2.Upload()
  file2['parents'] = [{"kind": "drive#parentReference", "id": folder_for_templates_id}]
  file2.Upload()

with open('assignments.csv', 'r', newline='') as assignments:
  reader = csv.reader(assignments, delimiter=';',quotechar='"')
  for row in reader:
    if row[0] == 'FILE_ID':
      continue 
    file_id = row[0]
    target_folder_id = row[1]
    file_to_copy = drive.CreateFile({'id': file_id})
    file_to_copy.Copy({'id': target_folder_id}, default_document_name)
    



