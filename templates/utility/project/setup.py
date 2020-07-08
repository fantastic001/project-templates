from distutils.core import setup
setup(
  name = '{{ project_name }}',
  packages = ['{{ project_name }}'],
  version = '0.1',
  description = '{{ description }}',
  author = '{{ author }}',
  author_email = '{{ email }}',
  url = '{{ url }}', # use the URL to the github repo
  download_url = '{{ url }}/tarball/0.1',
  keywords = [], 
  package_dir = {'{{ project_name }}': '{{ project_name }}'},
  classifiers = [],
  scripts = ["{{ project_name }}"],
  install_requires=["ArgumentStack", "jinja2"] # dependencies listed here 
)
