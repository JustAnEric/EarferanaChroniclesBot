import os, sys, json, re, requests

class Repository:
  """
  A repository class to interact with the Earferana Chronicles Bot GitHub.
  """
  def __init__(self, repo_url):
    self.repo = repo_url

  def get_version():
    get_new_ver = requests.get(f"https://raw.githubusercontent.com/{self.repo_url}/main/version").text
    return get_new_ver.partition('\n')[0]

  class current_folder:
    
