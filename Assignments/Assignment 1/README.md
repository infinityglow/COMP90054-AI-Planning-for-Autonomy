# COMP90054 AI Planning for Autonomy - Project 1 - Search 

You must read fully and carefully the assignment specification and instructions detailed in this file. You are NOT to modify this file in any way.

* **Course:** [COMP90054 AI Planning for Autonomy](https://handbook.unimelb.edu.au/subjects/comp90054) @ Semester 2, 2020
* **Instructor:** Dr. Nir Lipovetzky and Prof. Adrian Pearce
* **Deadline:** Friday 28th August, 2020 @ 11:59pm (end of Week 4)
* **Course Weight:** 10%
* **Assignment type:**: Individual
* **ILOs covered:** 1, 2, and 3
* **Submission method:** via git tagging (see Submission Instructions below for instructions)

The **aim of this project** is to get you acquainted with AI search techniques and how to derive heuristics in Pacman, as well as to understand the Python-based Pacman infrastructure.

 <p align="center"> 
    <img src="logo-p1.jpg" alt="logo project 1">
 </p>

## Your task

You **must build and submit your solution** using the sample code we provide you in this repository, which is different from the original [UC Berlkley code base](https://inst.eecs.berkeley.edu/~cs188/fa18/project1.html). If you want to provide a report with your submission (e.g., reflections, acknowledgments, etc.), please do so in file [REPORT.md](REPORT.md).

* Please remember to complete the [STUDENT.md](STUDENT.md) file with your individual submission details (so we can identify you when it comes time to submit). 

* You should **only work and modify** files [search.py](search.py) and [searchAgents.py](searchAgents.py) in doing your solution. Do not change the other Python files in this distribution.

* Your code **must run _error-free_ on Python 3.6**. Staff will not debug/fix any code. Using a different version will risk your program not running with the Pacman infrastructure or autograder and may risk losing (all) marks. You can install Python 3.6 from the [official site](https://www.python.org/dev/peps/pep-0494/), or set up a [Conda environment](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/) or an environment with [PIP+virtualenv](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/). 

* Your code **must not have carry any personal information**, like your student number or your name. That info should go in the [STUDENT.md](STUDENT.md) file, as per instructions above. If you use an IDE that inserts your name, student number, or username, you should disable that.

* **PacMan FAQ** is available to answer common questions you might about the project on Piazza at https://piazza.com/class/kd49qfdh119p6?cid=6

* **Getting started on GitHub** - this video explains how to **clone**, **git add**, **commit** and **push** while developing your solution for the project:
https://www.loom.com/share/ae7e93ab8bec40be96b638c49081e3d9

### Practice Task (0 marks)

To familiarise yourself with basic search algorithms and the Pacman environment, it is a good start to implement the tasks at https://inst.eecs.berkeley.edu/~cs188/fa18/project1.html, especially the first four tasks; however, there is no requirement to do so.

You should code your implentations *only* at the locations in the template code indicated by ```***YOUR CODE HERE***``` in files [search.py](search.py) and [searchAgents.py](searchAgents.py), please do not chage code at any other locations or in any other files.

### Part 1 (3 marks)

Implement the Iterative Deepening Search algorithm discussed in lectures, by inserting your code into the template indicated by the comment ```***YOUR CODE HERE FOR TASK 1***```, you can view the location at this link: [search.py#L117](search.py#L117).

You should be able to test the algorithm using the following command:

```
python pacman.py -l tinyMaze -p SearchAgent -a fn=ids
```

Other layouts are available in the layouts directory, and you can easily create you own!

### Part 2 (3 marks)

Implement the Enforced Hill Climbing algorithm discussed in lectures, using Manhattan Distance as the heuristic, by inserting your code into the template indicated by comment ```***YOUR CODE HERE FOR TASK 2***```, you can view the location at this link: [search.py#L127](search.py#L127).

Note that you don't have to implement Manhattan Distance, as this has already been implemented for you in the template code, although you will need to call the heuristic from inside your search. You should be able to test the algorithm using the following command:

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ehc,heuristic=manhattanHeuristic
```

Other layouts are available in the layouts directory, and you can easily create you own!


### Part 3 (4 marks) - Challenge Question (more difficult) 

This part involves solving a more complicated problem. Just like in Q7 of the Berkerley Pacman framework, you will be required to create an agent that will eat all of the food (dots) in a maze. Before doing so, however, the agent must eat a **Capsule** that is present in the maze. Your code should ensure that no food is eaten before the Capsule. You can assume that there is always exactly one Capsule in the maze, and that there will always be at least one path from Pacman's starting point to the capsule that doesn't pass through any food.

In order to implement this, you should create a new problem called `CapsuleSearchProblem` and a new agent called `CapsuleSearchAgent`. You will also need to implement a suitable `capsuleProblemHeuristic`. You may choose to implement other helper classes/functions. You should insert your code into the template indicated by the comments ```***YOUR CODE HERE FOR TASK 3***```, you can view the locations at these links: [search.py#L109](search.py#L109) and 4 positions in [searchAgents.py](searchAgents.py).

You should be able to test your program by running the following code (in one line):

```
python pacman.py -l capsuleSearch -p CapsuleSearchAgent
   -a fn=astar,prob=CapsuleSearchProblem,heuristic=capsuleProblemHeuristic
```

An agent that eats the capsule then proceeds to eat all of the food on the maze will receive 2 marks. The remaining 2 marks will be based on the performance of your agent (i.e. number of nodes expanded), as in Q7 of the Berkeley problem. Since you are using the A\* algorithm, however, the number of node expansions required for each grade will vary.

**Indicative marks** are shown below for node exapansions on the testing files [simpletest.test](test_cases_assignment1/advanced-part-3/simpletest.test) and [corner_tiny_corner.test](test_cases_assignment1/advanced-part-3/corner_tiny_corner.test) which are used by the autograder for checking your submission. Note that we will test your submission on different layouts, however this will give you a good guide for comparing the expected performance of your solution:

| simpletest (node expansions)     | Marks  | corner_tiny_corner (node expansions) | Marks | Total marks (Part 3) |
| ----------- | ----------- |  ----------- |  ----------- | ----------- |
| < 210      | 2       | < 2185 | 2 | 4 |
| > 210      | 1.75       | > 2185 | 1.75 | 3.5 |
| > 213      | 1.5        | > 3516 | 1.5 |  3 |
| > 644      | 1.25       | > 4558 | 1.25 | 2.5 |
| > 853   | 1        | > 5542 | 1 | 2 |

## Marking criteria

Marks are allocated according to the task breakdown listed above, based on how many of our tests the algorithms pass. No marks will be given for code formatting, etc. Observe that while the automarker is a useful indication of your performance, it may not represent the ultimate mark. We reserve the right to run more tests, inspect your code and repo manually, and arrange for a face-to-face meeting for a discussion and demo of your solution if needed.  You must **follow good SE practices**, including good use of git during your development such as:

* _Commit early, commit often:_ single or few commits with all the solution or big chucks of it, is not good practice.
* _Use meaningful commit messages:_ as a comment in your code, the message should clearly summarize what the commit is about. Messages like "fix", "work", "commit", "changes" are poor and do not help us understand what was done.
* _Use atomic commits:_ avoid commits doing many things; let alone one commit solving many questions of the project. Each commit should be about one (little but interesting) thing. 

## Checking your submission

Run the following command to run sanity checks using our test files:

```
python ./autograder.py --test-directory=test_cases_assignment1
```

It is important that you are able to run the autograder and have these tests pass, otherwise, our marking scripts will NOT work on your submission.

**NOTE**: You should not change any files other than [search.py](search.py) and [searchAgents.py](searchAgents.py). You should not import any additional libraries into your code. This risks being incompatible with our marking scripts.



## Submission Instructions

This repository serves as a start code for you to carry out your solution for [Project 1 - Search](http://ai.berkeley.edu/search.html) from the set of [UC Pacman Projects](http://ai.berkeley.edu/project_overview.html) and the marked questions. 

**To submit your assignment** you must complete the following three steps:

1. Complete the [STUDENT.md](STUDENT.md) file with your details of the submission.
2. Check that your solution runs on Python 3.6 and that your source code does not include personal information, like your student number or name. 
3. Tag the commit version you want to be graded with tag `submission`. 
    * The commit and tagging should be dated before the deadline.
    * Note that a tag is NOT a branch, so do not just create a branch called "submission" as that will not amount to tagging.
4. Fill the [Project 1 Certification Form](https://forms.gle/BzDH4ea5iennKbHe8).
    * Non-certified submissions will not be marked and will attract zero marks.
    


From this repository, we will copy *only* the files: [search.py](search.py) and [searchAgents.py](searchAgents.py). Please do not change any other file as part of your solution, or it will not run. Breaking these instructions breaks our marking scripts, delays marks being returned, and more importantly, gives us a headache. Submissions not compatible with the instructions in this document will attract zero marks and do not warrant a re-submission. Staff will not debug or fix your submission.

Please view the following to learn how to *Tag* your commit version you want to be graded:

**How to create a Tag using the Command Line**:
https://www.loom.com/share/17ec72b954454bc89bbe1dbb0bd2874f

**Another way to create a Tag using the User Interface**:
https://www.loom.com/share/3cd39e97919e4b688d9841613aba6973

## Important information

**Corrections:** From time to time, students or staff find errors (e.g., typos, unclear instructions, etc.) in the assignment specification. In that case, corrected version of this file will be produced, announced, and distributed for you to commit and push into your repository.  Because of that, you are NOT to modify this file in any way to avoid conflicts.

**Late submissions & extensions:** A penalty of 10% of the maximum mark per day will apply to late assignments up to a maximum of five days, and 100% penalty thereafter. Extensions will only be permitted in _exceptional_ circumstances; refer to [this question](https://docs.google.com/document/d/17YdTmDC54WHq0uZ-2UX3U8ESwULyBDJSD4SjKCrPXlA/edit?usp=sharing) in the course FAQs. 

**About this repo:** You must ALWAYS keep your fork **private** and **never share it** with anybody in or outside the course, except your teammates, _even after the course is completed_. You are not allowed to make another repository copy outside the provided GitHub Classroom without the written permission of the teaching staff. Please respect the [authors request](http://ai.berkeley.edu/project_instructions.html): 

> **_Please do not distribute or post solutions to any of the projects._**

**Academic Dishonesty:** This is an advanced course, so we expect full professionalism and ethical conduct.  Plagiarism is a serious issue. Please **don't let us down and risk our trust**. The staff take academic misconduct very seriously. Sophisticated _plagiarism detection_ software (e.g., [Codequiry](https://codequiry.com/), [Turinitin](https://www.turnitin.com/), etc.) will be used to check your code against other submissions in the class as well as resources available on the web for logical redundancy. These systems are really smart, so just do not risk it and keep professional. We trust you all to submit your own work only; please don't let us down. If you do, we will pursue the strongest consequences available to us according to the **University Academic Integrity policy**. For more information on this see file [Academic Integrity](ACADEMIC_INTEGRITY.md).

**We are here to help!:** We are here to help you! But we don't know you need help unless you tell us. We expect reasonable effort from you side, but if you get stuck or have doubts, please seek help. We will ran labs to support these projects, so use them! While you have to be careful to not post spoilers in the forum, you can always ask general questions about the techniques that are required to solve the projects. If in doubt whether a questions is appropriate, post a Private post to the instructors.

**Silence Policy:** A silence policy will take effect **48 hours** before this assignment is due. This means that no question about this assignment will be answered, whether it is asked on the newsgroup, by email, or in person. Use the last 48 hours to wrap up and finish your project quietly as well as possible if you have not done so already. Remember it is not mandatory to do all perfect, try to cover as much as possible. By having some silence we reduce anxiety, last minute mistakes, and unreasonable expectations on others. 

Please remember to follow all the submission steps as per project specification.

## COMP90054 Code of Honour

We expect every UoM student taking this course to adhere to it **Code of Honour** under which every learner-student should:

* Submit their own original work.
* Do not share answers with others.
* Report suspected violations.
* Engage in any other activities that will dishonestly improve their results or dishonestly improve or damage the results of others.

Unethical behaviour is extremely serious and consequences are painful for everyone. We expect enrolled students/learners to take full **ownership** of your work and **respect** the work of teachers and other students.


**I hope you enjoy the project and learn from it**, and if you still **have doubts about the project and/or this specification** do not hesitate asking in the [Piazza Course Discussion Forum](https://piazza.com/unimelb.edu.au/fall2020/comp90054/home) and we will try to address it as quickly as we can!

**GOOD LUCK and HAPPY PACMAN!**

## Acknowledgements

This is [Project 1 - Search](http://ai.berkeley.edu/search.html) from the set of [UC Pacman Projects](http://ai.berkeley.edu/project_overview.html).  We are very grateful to UC Berkeley CS188 for developing and sharing their system with us for teaching and learning purposes.
