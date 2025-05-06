# Welcome to Day 2!

Today, we’ll dive into two hands-on exercises to further sharpen your git skills:

<details>
<summary>Activity 1 - Cloning from remote</summary>

# 🔧 Cloning from remote

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

# 🛠️ Cloning from remote (Step-by-Step)

## 1. 🔱 Fork the Repository

You probably already have a fork of the course repo. Skip if you have.
Below you are given two options to clone from remote:


<details>
<summary>Activity 1 Option 1 - Using the command line</summary>

## 2. 💻 Clone Your Fork (make a local copy)

This option uses the terminal (MacOS, UNIX, Gitbash)

> NOTE: if you use WINDOWS, install GitBash first. Execute all commands in GitBash.

Open a terminal (locally) and run:

```bash
git clone git@github.com:your-username/repo-name.git
```

Replace `your-username` and `repo-name` with your actual GitHub username and repository name.  

You can also copy the url from the green `CODE` button on Github online.

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

You can also edit the file in any other code or file editor.

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

That’s it! You've submitted your contribution.

</details>

<details>
<summary>Activity 1 Option 2 - Using Github Desktop</summary>

### 2.▶️ Clone Directly from GitHub

1. Go to your forked repository on [GitHub.com](https://github.com).
2. Click the green **"Code"** button.
3. In the dropdown, click **"Open with GitHub Desktop"**.
4. This will launch **GitHub Desktop** and ask you where to save the local copy.
5. Choose your local path and click **Clone**.

> 💡 You can use **HTTPS** or **SSH** — both work. Make sure your GitHub Desktop is set up with the correct credentials (especially for SSH).

## 3. 📂 Open the Project Directory

After cloning, GitHub Desktop automatically loads the project.

- You can open the local folder via **Repository → Show in Finder/Explorer**.
- Or open it in a code editor like VSCode or PyCharm.

---

## 4. 🔧 Make Some Changes

Edit your files using any editor you like (e.g., VSCode, Sublime, Atom).

Example changes:

- Edit `README.md`
- Add a new script
- Fix a bug in a Python file

GitHub Desktop will automatically detect changes.

---

## 5. ✅ Stage and Commit the Changes

1. Go to **GitHub Desktop**.
2. See all file changes under the **Changes** tab.
3. Add a **summary** for the commit (e.g., `Update README`).
4. Click **Commit to `main`** (or whichever branch you’re working on).

---

## 6. 🚀 Push to Your Fork (GitHub Remote)

1. After committing, click the **Push origin** button in the top bar.
2. Your changes will be uploaded to your GitHub repository.

> ✅ You can confirm your changes on GitHub by refreshing the repo page.

## 7. 🔁 Make a Pull Request

1. Go to **your fork** on GitHub.
2. Click **"Compare & pull request"**.
3. Make sure the base repository is the instructor’s original repo.
4. Write a meaningful title and description.
5. Click **"Create pull request"**.

---

That’s it! You've submitted your contribution.

</details>

</details>

<details>
<summary>Activity2 - Adding a remote</summary>

# 🔗 Adding a Remote to a lcoal Git Repository

This guide walks you through connecting a local project to a remote repository on GitHub using either the **Terminal** or **GitHub Desktop**.

<details>
<summary>Activity 2 Option 1: Adding a remote using the Terminal</summary>

# 🖥️ Version 1: Using the Terminal (Command Line)

## 1️⃣ Create a New Remote Repository on GitHub

> ✅  If you want to push a local repository to Github using the Command line, you  have to create an empty online target repository first.

1. Go to [https://github.com](https://github.com).
2. Click the **“+”** in the top right → **New repository**.
3. Name your repository (e.g., `my-project`).
4. Choose **Public** 
5. **Do not** initialize with a README, `.gitignore`, or license if pushing an existing repo.
6. Click **Create repository**.
7. Copy the repo URL (either **HTTPS** or **SSH**) from the next page.

## Connect your local project/folder

For the sake of this exercise, you can create a simple folder with a test file.

```bash
cd path/to/your/project       # move into your folder
git init                      # Initialize Git repo if not already done
git add .                     # Stage all files
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git branch -M main            # Rename default branch to main
git push -u origin main       # Push code to GitHub
```

</details>

<details>
<summary>Activity 2 Option 2: Adding a remote using Github Desktop</summary>


## 🖱️ Version 2: Using GitHub Desktop

###  Connect/Publish/Push your local folder
1. Open **GitHub Desktop**.
2. Go to **File → Add Local Repository**.
3. Choose your folder and click **Add Repository**.
4. Click **Publish repository** (top bar).
5. Fill in name and description.
6. Choose "Private" if needed.
7. Click **Publish Repository** — GitHub Desktop sets up the remote and pushes.


> ✅ GitHub Desktop automatically connects the local and remote repositories.

</details>

</details>

 <br>
We will also work on  hands-on exercises to practice good coding practices:<br><br>

<details>
<summary>Activity3 - Setting up and organizing a coding project</summary>

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
**pycache**/
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

> ✨ Tip: Write clear function names and use code comments to describe what your functions do.

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
<br>
<a target="_blank" href="https://colab.research.google.com/github/likeajumprope/RSE_Juelich/blob/main/day2/Day2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
