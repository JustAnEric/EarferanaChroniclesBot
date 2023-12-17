import os, sys, json, re, requests

current_repo = None

class Repository:
  """
  A repository class to interact with the Earferana Chronicles Bot GitHub.
  """
  def __init__(self, repo_url):
    self.repo =repo_url
    current_repo =repo_url

  def get_version():
    get_new_ver = requests.get(f"https://raw.githubusercontent.com/{self.repo_url}/main/version").text
    return get_new_ver.partition('\n')[0]

  def get_queries():
    get_new_quer = requests.get(f"https://raw.githubusercontent.com/{self.repo_url}/main/queries").text
    return get_new_quer.split(', ')

  class current_folder:
    def update_files(queries=[]):
      if len(queries) == 0:
        return print("[*GIT] No queries to update!")
      else:
        for query in queries:
          query_url = f"https://raw.githubusercontent.com/{self.repo_url}/main/{query}"
          print(f"[-GIT] Updating query {query} with query URL : {query_url} ...")
          query_req = requests.get(query_url).text
          if os.path.exists(query):
            # continue
            open(f'{query}','w').write(query_req)
          else:
            # make the file then continue
            open(f'{query}','w').write(query_req)
            print(f"| - [GIT.WARNING] Query file {query} does not exist. Making the file then adding data.")
        print("Finished updating queries.")
