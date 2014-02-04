norsk_NoW
=========

mnemosine (http://mnemosyne-proj.org/) vocabulary for NoW course

stupid simple usage:

1. download the norsk_chapterx_topic.txt files you want (easiest through "Download ZIP", on the right)
2. fire up mnemosine
3. import from file (tab-separated text files)
4. use the file name as tag, replace '_' by '::', e.g.
   file 'norsk_chapter1_numbers.txt' => tag 'norsk::chapter1::numbers'
5. have fun and check again for updates ;)

stupid simple updates:

1. create/change update your vocabulary
2. use Ctrl+D to open the deactivate cards dialog
3. uncheck "All tags" on the right, and make sure that "having any of these tags" is selected
4. check the tag you want to export (leaf of the tree)
5. close the dialog with ok
6. use file, export to export a tab-separated text file
7. use the naming scheme as above, e.g.
   tag 'norsk::chapter1::numbers' => file 'norsk_chapter1_numbers.txt'
8. send me the file, I'll check it into the repo (if it's good :p)

better usage (you'll need to learn some really handy stuff, though)

1. use git, make yourself familiar with it. an easy start could be http://rogerdudler.github.io/git-guide/
2. git clone https://github.com/greuters/norsk_NoW.git
3. create a fork and send me pull requests, if you want to modify

=> you'll get all the advantages of version control:

- complete control over the updates you pull and want/don't want to use from my repo
- your own modifications, as you want them (e.g. non-swiss-german-style pronounciation hints)
- automatic difference comparisons, and a complete history of all versions of the vocabulary
- could be handy for any following latex thesis etc..

