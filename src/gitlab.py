import gitlab

def get_mr_commit_history(project_id: int, mr_id: int, private_token: str | None = None, gitlab_url: str = "https://gitlab.com") -> list[str]:
    """
    Return a list of commit titles for a given MR.

    Args:
        project_id (int): The project ID.
        mr_id (int): The MR id.
        private_token (str): A private token for authenticated use of the GitLab API.
        gitlab_url (str): The base url of your gitlab deployment. Defaults to https://gitlab.com.
    
    Returns:
        list[str]: List of commit titles.
    """
    gl = gitlab.Gitlab(gitlab_url, private_token=private_token)
    project = gl.projects.get(project_id)
    mr = project.mergerequests.get(mr_id)
    source_branch = mr.source_branch
    commits = project.commits.list(ref_name=source_branch)
    commit_titles = [commit.title for commit in commits]
    return commit_titles
