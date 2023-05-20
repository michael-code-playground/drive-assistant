# Template organiser - concept

As a person that uses Google Drive on a daily basis, makes a lot of notes and stores them in various templates, I thought it'd wise to offload some work involving copying/renaming/sorting files as it can easily be automated. For some reason, Google Drive doesn't provide an option to create your own set of templates, save them, and select each time you create a new document. My motivation was to create a script that would help my manage my files, rename them (typically to a data created) and assign to proper folders to keep my drive well-organised, as I've noticed when the number of files grows, things can get out of control pretty quickly.

# My way to handle the problem

I've created a folder named TEMPLATES which is meant to store my templates as the name suggests. The script runs the query where it searches the whole drive for files that may be identified as possible templates. Ideally I'd put a parameter in a query 'name contains 'template'', however, using that parameter, every query fails (I haven't yet figured out why). Instead I've changed the parameter to 'fullText contains 'template', and set the visibility to limited to narrow results. Once files have been found, they're moved to 'TEMPLATES'. It ensures that templates are not scattered across the whole drive. Also, I follow a few common patterns when it comes to using some of my templates, that's why I created an additional csv file (assignments.csv) consisting of two columns, the first one features IDs of those templates, and the second one IDs of dictionaries where I eventually put them to, once editing is done. The script copies chosen files to folders specified by me in the file and renames them to current date when I run it - such a nomenclature helps me optimse my workflow and makes it way easier to find a particular file.

# Ideas to customise

The script is pretty straightforward and fully adaptable to meet different requirements. Query may be modified, files may be moved to any other location specified by a user, the way to name files may also be changed. I'd be happy if someone else found it useful and come up with further ideas how to extend the idea. 
