# Week 1
---

## Day 1

`Python`: Created a somewhat more complicated Hello World, which asks for the users name via a
function call prior to printing their name. A nice little start while getting lessons and
environments set up.

`BASH`: Created the folder structure script which will help to automate making folders and
readme's for the following weeks. Was nice to brush up on very basic bash scripting for
the first day as well.

## Day 2
`Python`: Created a Current Working Directory listing applicating similar to `ls` which
prompts user for a search criteria (such as a name like `README`, or type such as `py`,
`.py`, `.cpp`, etc.). It then displays the appropriate results. This is my introduction
to Python 3.5's string.`format`, which I probably abused too much in this one. I also
worked with the `fnmatch` libray for filename comparing.

## Day 3:
`Python`: Learned about the concept of `__init__.py`, which is best discussed here:
www.reddit.com/r/Python/comments/1bbbwk/whats_your_opinion_on_what_to_include_in_init_py/.
Also started to learn about Pythonic preferences and coding guidelines, which will be
demonstrated over the weekend.

`BASH`: Added `__init__.py` to generator script.

## Day 4: 
`Python`: First introduction to using pip to install dependencies, watching it break on Ubuntu 18.04 (can be read more here as to potential reasons: https://github.com/pypa/pip/issues/5240) while trying to install pipenv which I understand to similar to `npm`. Interacted with `requests` module to do basic get request, and from there building a dog breed image gallery.

## Day 5: 
`Python`: First introduction to Python classes, working more with the Dogs model which was described from Day 4's little project. 
This also introduced me to more string manipulation using the offical built in functions and even some functional programming!.

## Day 6: 
`Python`: Purely a research dirven day learning best practices and 'best' ways of accomplishing certain tasks such as file opening, scopes, and object management. Discovered quite a few useful resources such as: 
- http://docs.python-guide.org/en/latest/writing/style/
- https://www.cs.cmu.edu/~srini/15-441/F11/lectures/r04-python.pdf
- https://github.com/mikeckennedy/write-pythonic-code-demos/tree/master/code/ch_01_pep8
- pep8 (linting standard)

This was applied to Day 6's update of the Day 4 API Poller.

## Day 7: 
`Python`: Applied similar pythonic fixes to the Dog Class implementation from Day 5, also installing pep8, pycodestyle and a few modules which I hope to use in the coming days too! I recommend installing the following for VSCode if you are using it for Python Development: 
- Python by Microsoft   => Python Language Support
- Code Runner by Jun Han => Code Execution / Interpreter 
- Magic Python by MagicStack Inc. => Syntax Highlighting for Modern Projects
- Better Comments => Better Comment Highlighting