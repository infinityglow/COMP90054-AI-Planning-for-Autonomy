# COMP90054 AI Planning for Autonomy - Additional Project - Reinforcement Learning 

You must read fully and carefully the assignment specification and instructions detailed in this file. You are NOT to modify this file in any way.

* **Course:** [COMP90054 AI Planning for Autonomy](https://handbook.unimelb.edu.au/subjects/comp90054) @ Semester 2, 2020
* **Instructor:** Dr. Nir Lipovetzky and Prof. Adrian Pearce
* **Deadline:** Monday 26th October, 2020 @ 11:59pm (start of Week 12)
* **Course Weight:** 5% (Additional)
* **Assignment type:**: Individual
* **ILOs covered:**  2, 3, 4 and 5
* **Submission method:** via git tagging (see Submission Instructions below for instructions)

The **aim of this project** is to get you acquainted with value iteration and reinforcement learning, which is a good practise to have if you intended to do this for the pacman-contest.

 <p align="center"> 
    <img src="logo-p3.png" alt="logo project 3">
 </p>

## Your task

You **must build and submit your solution** using the sample code we provide you in this repository, which is the same from the original [UC Berlkley code base](https://inst.eecs.berkeley.edu/~cs188/su20/project3/). If you want to provide a report with your submission (e.g., reflections, acknowledgments, etc.), please do so in file [REPORT.md](REPORT.md).

* Please remember to complete the [STUDENT.md](STUDENT.md) file with your individual submission details (so we can identify you when it comes time to submit). 

* You should **only work and modify** files [valueIterationAgents.py](valueIterationAgents.py), [qlearningAgents.py](qlearningAgents.py) and [analysis.py](analysis.py) in doing your solution. Do not change the other Python files in this distribution.

* Your code **must run _error-free_ on Python 3.6**. Staff will not debug/fix any code. Using a different version will risk your program not running with the Pacman infrastructure or autograder and may risk losing (all) marks. You can install Python 3.6 from the [official site](https://www.python.org/dev/peps/pep-0494/), or set up a [Conda environment](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/) or an environment with [PIP+virtualenv](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/). 

* Your code **must not have carry any personal information**, like your student number or your name. That info should go in the [STUDENT.md](STUDENT.md) file, as per instructions above. If you use an IDE that inserts your name, student number, or username, you should disable that.

* **PacMan FAQ** is available to answer common questions you might about the project on Piazza at https://piazza.com/class/kd49qfdh119p6?cid=6

* **Getting started on GitHub** - this video explains how to **clone**, **git add**, **commit** and **push** while developing your solution for the project:
https://www.loom.com/share/ae7e93ab8bec40be96b638c49081e3d9

* This assignment is worth **5%** of your final mark **(aditionaly)**.

## Tasks
The details of each tasks are givin in the original [UC Berlkley code base](https://inst.eecs.berkeley.edu/~cs188/su20/project3/). Each task will help your understand more about the related subject content. 

## Marking criteria

Marks are allocated based on how many of our tests the algorithms pass (divided by 5). No marks will be given for code formatting, etc. Observe that the automarker is a useful indication of your performance, it should represent the ultimate mark. We will copy those three required files, and run it on our server. We reserve the right to inspect your code and repo manually, and arrange for a face-to-face meeting for a discussion and demo of your solution if needed.  You must **follow good SE practices**, including good use of git during your development such as:

* _Commit early, commit often:_ single or few commits with all the solution or big chucks of it, is not good practice.
* _Use meaningful commit messages:_ as a comment in your code, the message should clearly summarize what the commit is about. Messages like "fix", "work", "commit", "changes" are poor and do not help us understand what was done.
* _Use atomic commits:_ avoid commits doing many things; let alone one commit solving many questions of the project. Each commit should be about one (little but interesting) thing. 

## Checking your submission

Run the following command to run sanity checks using our test files:

```
python ./autograder.py
```

It is important that you are able to run the autograder, it indicates your final marks.

**NOTE**: You should not change any files other than [valueIterationAgents.py](valueIterationAgents.py), [qlearningAgents.py](qlearningAgents.py) and [analysis.py](analysis.py) . You should not import any additional libraries into your code. This risks being incompatible with our marking scripts.



## Submission Instructions


**To submit your assignment** you **must** complete the following four steps:

1. Complete the [STUDENT.md](STUDENT.md) file with your details of the submission.
2. Check that your solution runs on Python 3.6 and that your source code does not include personal information, like your student number or name. 
3. Tag the commit version you want to be graded with tag `submission`. 
    * The commit and tagging should be dated before the deadline.
    * Note that a tag is NOT a branch, so do not just create a branch called "submission" as that will not amount to tagging.
4. Fill the [Project RL (Additional) Certification Form](https://forms.gle/gjK7hGM5HLdwTwzQ6).
    * Non-certified submissions will not be marked and will attract zero marks.
    


From this repository, we will copy *only* the files: [valueIterationAgents.py](valueIterationAgents.py), [qlearningAgents.py](qlearningAgents.py) and [analysis.py](analysis.py). Please do not change any other file as part of your solution, or it will not run. Breaking these instructions breaks our marking scripts, delays marks being returned, and more importantly, gives us a headache. Submissions not compatible with the instructions in this document will attract zero marks and do not warrant a re-submission. Staff will not debug or fix your submission.

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

This is [Project 3: Reinforcement Learning](https://inst.eecs.berkeley.edu/~cs188/su20/project3/) from the set of [UC Pacman Projects](https://inst.eecs.berkeley.edu/~cs188/su20/projects/#projects-overview).  We are very grateful to UC Berkeley CS188 for developing and sharing their system with us for teaching and learning purposes.
