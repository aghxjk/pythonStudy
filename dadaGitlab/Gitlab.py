from gitlab import Gitlab
###############################
# 需要安装的依赖库
# pip install python-gitlab
###############################

url = 'https://gitlab.dadaabc.us'

# login gitlab
gl = Gitlab(url, None, "jeremy.zhao@dadaabc.net", "kele.1025")

# get all projects
projects = gl.projects.list(all=True)

# print all projects

for pro in projects:
    print(pro.ssh_url_to_repo)

