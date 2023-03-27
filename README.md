# 自動建立新 Github repository

## 簡單的 Bash script ＋ Python 爬蟲練習

把每次新增專案的流程自動化，在 terminal 輸入 `create [專案名稱]`就可以做到以下流程： </br>

`新增資料夾 --> git init --> 新增git repo --> git remote 等 --> 開啟vscode`

```
[20230327更新]:
若Github有設定兩步驟驗證，會無法使用網頁爬蟲的方式新增並連結到github repo，只能改用script建立local repo並等待使用者輸入git remote url。
```

# Automatically create a new Github repository by a simple command

## Simple bash script & Python Web Scraping practice

Automate my process of creating a new project with entering `create-github <project name>` in terminal to achieve the following process:

`create project folder --> git init --> create git repository --> git remote etc. --> open vscode`

## How to use
Custom command has two function:
- `create()`: Only create a new local repository, you need to enter remote repository url (e.g. github/gitlab) by yourself.
- `create-github()`: If you haven't set up two-way authentication, you can use this function to create a new repository and link it to github automatically.

Steps:
1. Create a new folder for your custom command
2. Copy `.my-cmd.sh` to the folder you create
3. Open `.my-cmd.sh` in any kind to text editor you prefer, and change the following variable to your local setting.
   - `CMDIR`: your custom command folder path
   - `PROJECT_ROOT`: your project root path
4. Add execution permission
```bash
chmod +x .my-cmd.sh
```
1. Add custom command to `~/.zshrc`
  
```bash
vim ~/.zshrc
# add 
source ~/your-custom-command-folder-path/.my-cmd.sh
```
6. Source zshrc
```bash
source ~/.zshrc
```

Then you can run the commands in `my-cmd.sh` by using th following command:
```
create <project-name>
```
OR
```
create-github <project-name>
```

## Result

![image](https://github.com/ariel7234/repo_create/blob/main/img/result.gif)

## 參考資料

- [How to create your own Custom Terminal Commands](https://medium.com/devnetwork/how-to-create-your-own-custom-terminal-commands-c5008782a78e)
