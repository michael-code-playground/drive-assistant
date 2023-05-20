# Template organiser - concept

As a person that uses Google Drive on a daily basis, makes a lot of notes and stores them in various templates, I thought it'd wise to offload some work involving copying/renaming/sorting files as it can easily be automated. For some reason, Google Drive doesn't provide an option to create your own set of templates, save them, and select each time you create a new document. My motivation was to create a script that would help my manage my files, rename them (typically to a data created) and assign to proper folders to keep my drive well-organised, as I've noticed when the number of files grows, things can get out of control pretty quickly.

# My way to handle the problem, ideas to customise

I've created a folder named TEMPLATES which is meant to store my templates as the name suggests. The script runs the query where it searches the whole drive for files that may be identified as possible templates. Ideally I'd put a parameter in a query 'name contains 'template'', however, using that parameter any query fails (I haven't yet figured out why), instead a change the parameter to 'fullText contains 'template')
