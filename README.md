# 🐙 GitHub Activity CLI  

A simple command-line interface that fetches and displays a GitHub user's recent activity straight in your terminal.  

This project is perfect for practicing:  
- Working with APIs  
- Handling JSON data  
- Building CLI applications  

---

## ✨ Features  

- Fetches recent activity of any GitHub user  
- Displays activity in a human-friendly way  
- Supports multiple event types (Push, Issues, Watch, Pull Requests, etc.)  
- Summarizes commit counts for repositories  
- Handles invalid usernames and API errors gracefully  

---

## ⚡ Requirements  

- Python 3.11 
- Standard library (`argparse`)  
- `requests` library (for API calls)  

---

## 📦 Installation  

Clone this repository and move into the project directory:  

```bash
git clone https://github.com/simply-blessing/github-activity-cli.git
cd github-activity-cli

--- 

## 🚀 Usage

python git_activity.py <username>

Example:

python git_activity.py simply-blessing

Output:

Here is simply-blessing recent activity:

* Pushed 3 commits to Simply-Blessing/TaskPad
* Created branch main
* Created repository TaskPad
* Starred florinpop17/app-ideas
* Forked imnowdevops/ddc-material


---

## Roadmap Project

https://roadmap.sh/projects/github-user-activity