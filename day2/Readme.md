Welcome to Day 2, Chantal!

Today, we’ll dive into two hands-on exercises to sharpen your collaboration and coding skills:


<details>
<summary>Activity 1 - More Git</summary>

# 🔧 Exercise 1: More Git


<details>
<summary>Optional - setting up a ssh key</summary>

## 🔐 Setting Up SSH for GitHub (Optional but Recommended)

### 0.1 🔍 Check for Existing SSH Keys

```bash
ls -al ~/.ssh
```

Look for files like `id_ed25519.pub` or `id_rsa.pub`. If they exist, you might already have a key.

---

### 0.2 🧾 Generate a New SSH Key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter to accept the default file location. Optionally, add a passphrase for security.

---

### 0.3 🧠 Add the Key to the SSH Agent

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

---

### 0.4 📋 Copy the Public Key

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the output.

---

### 0.5 🌐 Add the SSH Key to GitHub

1. Go to GitHub → Profile → **Settings**
2. Navigate to **SSH and GPG Keys**
3. Click **New SSH Key**
4. Paste your public key and save

---

### 0.6 🧪 Test the Connection

```bash
ssh -T git@github.com
```

You should see a success message like:

```bash
Hi your_username! You've successfully authenticated...
```
</details>

# 🛠️ Contributing to This Project (Step-by-Step)

## 1. 🔱 Fork the Repository

Go to the original repository on GitHub (provided by your instructor) and click the **"Fork"** button in the top-right corner.  
This will create **your own copy** of the repository under your GitHub account.

---

## 2. 💻 Clone Your Fork

Open a terminal and run:

```bash
git clone git@github.com:your-username/repo-name.git
```

Replace `your-username` and `repo-name` with your actual GitHub username and repository name.  
If you're using HTTPS instead of SSH:

```bash
git clone https://github.com/your-username/repo-name.git
```

---

## 3. 📂 Change into the Project Directory

```bash
cd repo-name
```

---

## 4. 🔧 Make Some Changes

Edit one or more files using your favorite code editor (e.g., VSCode, nano, etc.).  
For example:

```bash
nano yourfile.md
```

---

## 5. ✅ Stage and Commit the Changes

```bash
git add .
git commit -m "Made some changes to my file"
```

---

## 6. 🚀 Push to Your Fork (Origin)

```bash
git push origin main
```

Use the branch name you're working on (e.g., `main`, `dev`, or `feature-branch`).

---

## 7. 🔁 Make a Pull Request

1. Go to **your fork** on GitHub.
2. Click **"Compare & pull request"**.
3. Make sure the base repository is the instructor’s original repo.
4. Write a meaningful title and description.
5. Click **"Create pull request"**.

---

That’s it! You've submitted your contribution. 

</details>

<details>
<summary>Activity2 - Setting up and organizing a coding project</summary> 


# 🧪 Mini Project (Day 2): Analyzing Study Habits and Performance

Welcome to your group project! Today you will apply research software engineering principles to a mini analysis project.

## 🧩 Scenario

You are provided with a dataset named `student_habits_performance`.csv.
Your task is to analyze the relationship between hours studied per day and exam scores, and produce a short, reproducible report following good software engineering practices.

You may use your favorite programming language, but it is recommended to use Python.

You can run the provided Jupyter notebook template here:

<a target="_blank" href="https://colab.research.google.com/github/likeajumprope/RSE_Juelich/blob/main/day2/Day2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


> ⚠️ **Warning:** Jupyter notebooks opened directly in the browser **do not save your work!**
To avoid losing progress, **save a copy to your Google Drive** (if logged into a Google account) or **download a local copy.**




---

## 📁 Step 1: Create a Project Folder Structure

Organize your project like this:

```student-habits-project/
├── data/
│   ├── raw/              # Original dataset goes here (unchanged)
│   └── clean/            # Cleaned/processed data
├── src/                  # Python scripts (e.g., cleaning, analysis, plotting). 
├── results/              # Output files like figures or tables
├── report/               # Markdown summary and written interpretation
├── .gitignore            # Files/folders to ignore in version control
├── README.md             # Project overview and how to run it
```
> 📌 **Tip**: Never modify the raw data directly. Always save processed data to `data/clean/`.

---

## 🧬 Step 2: Initialize Version Control with Git

We will practice using git in the Jupyter notebook. In Jupyter notebook, you can write system commands with `!` at the beginning of the line.

For example: 

` ! command `

1. Initialize a git repository

`!git init`

2. Check the status of your repository:

`!git status`

## 📝 Step 3: Create a README.md for your project
Create a README.md file for your project.
It should include:
- Project title and description
- Instructions on how to run your scripts
- Dependencies and setup instructions


## 🚫 Step 4: Modify your .gitignre file

Edit your .gitignore to exclude raw data and system-specific files.
Example:

An example could look like:

data/raw/
__pycache__/
*.ipynb_checkpoints/



## 💾 Step 5. Commit your code regularly 

Use meaningful commit messages:

! git add .
! git commit -m "Initial commit: project structure"

## 🛠️ Step 6: Write modular functions

### Step 6.1: clean your data
Write a function to clean your data one of the cells of the Jupyter notebook.
Write a function `clean_data.py` in `src`. 

In both cases:
- Load the dataset (`data/raw/student_habits_performance.csv`) using `pandas`
- Handle missing values (e.g., drop rows with NaN)
- Save the cleaned dataset to `data/clean/cleaned_data.csv`

✨ Tip: Write clear function names and use docstrings to describe what your functions do.

If needed, install libraries using:

`!pip install pandas`

>  ✨ Tip: Write clear function names and use code comments to describe what your functions do.

## 📊 Step 6.2: Visualize study  habits
- Create a function that visualizes study habits. Do it again, first in the cell of the Jupyter notebook. Then create a file src/plot_mydata.py for it.

In both cases:
- Use `matplotlib` to visualize study habits
- Save your figure to results/study_habits.png
- Include axis labels, a title, and a legend if needed

> ✍️ Add a code comments to your plotting function and comment the main steps (e.g., load data, create figure, save figure).

## 📝 Step 7: Write a Summary Report

Create a file:
report/study_habits.md

Your report should:
- Briefly summarize your findings
- Include your figure (link it using Markdown)

Example of linking a figure in markdown:

`![Study Habits by Gender](../results/study_habits.png)`

## ⚙️ Step 8:  Document your environment
Export your code to a requirements.txt file

`!pip freeze > requirements.txt`

## Step 9. Create a make file 

Create a simple Makefile to automate steps such as cleaning, running analysis, and generating figures.

Example structure:

`all: clean_data plot_data

clean_data:
	python src/clean_data.py

plot_data:
	python src/plot_mydata.py`

## ✅ Step 10: Final Checklist
Make sure your project:
- Uses a clean and modular folder structure
- Preserves raw data without modification
- Contains code with comments
- Organizes scripts in src/ with meaningful function names
- Uses Git with meaningful commit messages
- Excludes raw data and temporary files using .gitignore
- Saves a figure in results/ with proper labels
- Provides a short Markdown report linking the figure
- Documents the environment (e.g., requirements.txt)

</details>

<a target="_blank" href="https://colab.research.google.com/github/likeajumprope/RSE_Juelich/blob/main/day2/Day2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
