# ParallelProgrammingProject
Threaded UI application for displaying web pages

Write a Python program which uses a simple GUI for displaying web pages. The GUI should have four
elements: A field to enter a URL, a button to send of the URL, and two elements displaying html pages.
You can use a GUI library of your choice. Note that many libraries offer options to display html pages, so
we would recommend using one which does. You are not required to write rendering code yourself.
Also, high quality of the display is not essential, as long as the pages are visible.
The program should show two pages in parallel. Both displays are refreshed automatically. This is done
in intervals of 60 seconds. Initially, no pages are displayed and no refresh is done.
If the button is hit, the page is displayed in one of the displays. The display is chosen by which display
has not been refreshed for longer. If both have the same “age”, a random display can be chosen (this is
also true if both are still empty).
Hitting the button should no block the GUI, i. e. it should be possible to start typing a new URL whilst the
former one is fetched. If a page is being loaded whilst a refresh is scheduled, the refresh should still
start.
A typical run would look like this:
- Both displays empty.
- URL entered and button hit: First display shows and first clock starts ticking
- After 60 seconds, first display is refreshed
- URL entered and button hit: Second display shows and second clock starts ticking
- URL entered and button hit: Since first display is “older”, first display shows and first clock is
reset
- 60 seconds after second display was used, it is refreshed
- Continue
We will look for the following for marking:
- Working application
- Proper use of concurrency libraries
- Fluidity of user interface
- Proper use of comments to clarify the working of the program. You can also include a separate
document, if you wish, but we do not expect an essay
