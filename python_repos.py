import requests

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('status code:',r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()
print("total repositories:",response_dict['total_count'])

# #处理结果
# print(response_dict.keys())

#探索有关仓库的信息
repo_dicts = response_dict['items']
print('repositories return',len(repo_dicts))

#研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nselected information about each repository:")
for repo_dict in repo_dicts:
    print("\nselected infotmation about first repository:")
    print('name:',repo_dict['name'])
    print('owner:',repo_dict['owner']['login'])
    print('stars:',repo_dict['stargazers_count'])
    print('repository:',repo_dict['html_url'])
    print('created:',repo_dict['created_at'])
    print('updated:',repo_dict['updated_at'])
    print('description:',repo_dict['description'])
