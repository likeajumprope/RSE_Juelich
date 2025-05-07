# Reproducible Research Project - Day 3

Welcome to Day 3 of the Research Software Engineering Course!

In this session, you will practice making your research code reproducible, testable and automated.
You will complete two tasks.

Activity 1: Introduction to Testing.
Activity 2: Introduction to Github actions


<details>
<summary>Activity 1 - Introduction to Testing</summary>

# Activity 1: Introduction to Testing

You will work inside the provided Jupyter notebook and complete a series of tasks

<a target="_blank" href="https://colab.research.google.com/github/likeajumprope/RSE_Juelich/blob/main/day3/reproducible-research-project_day_3/notebooks/Day3.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Carefully read the instructions in the notebook. Here is an overview about what you will do:

1. First you will write inline `assert` startements for two functions, one that tests the number of rows in your data frame and one that tests that the data frame has no NaNs.

2. Then you will wrap these assert statements into functions and run them from within the Jupyter notebook.

3. Next, you will create a dedicated `test` folder in the root of your `research project folder`.  You will create two files, one for each test function that you have created. You will then run these functions from the Jupyter notebook command line using `pytest`.

4. You will create a Makefile and add the `pytest` command into it. You can now run the tests from the mMakefile.

Careful: your work will not automatically be saved. If you want to save it, you can `Create a copy on your Google Drive`

</details>

<details>
<summary>Activity 2: Introduction to Github actions</summary>

# Activity 2: Introduction to Github actions

## Add a github action workflow

You’ll find a workflow .yaml file in your Day 3 repository.

This file schedules the creation of an issue at the beginning of the month.

## Set the workflow up:

1.	On Github, in the root of the course project, create a folder named .github/workflows.
2.	Move the YAML file into that folder.
3.	Push the changes to GitHub.

Run the workflow manually:
4.	Go to the Actions tab on GitHub and run the workflow manually.

</details>