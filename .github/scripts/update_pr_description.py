from os import environ
from re import sub

from github import Github

token = environ['GITHUB_TOKEN']
repo_name = environ['GITHUB_REPOSITORY']
pr_number = int(environ['PR_NUMBER'])
preview_url = environ['PREVIEW_URL']

gh = Github(token)
repo = gh.get_repo(repo_name)
pr = repo.get_pull(pr_number)

preview_label = '📚 Documentation preview 📚: '
preview_text = f'{preview_label} {preview_url}'
current_body = pr.body or ''

if preview_label in current_body:
    new_body = sub(
        f'{preview_label}.*',
        preview_text,
        current_body,
    )
else:
    new_body = (
        f'{current_body}'
        '\n\n---\n\n'
        f'{preview_text}'
    )

pr.edit(body=new_body)
