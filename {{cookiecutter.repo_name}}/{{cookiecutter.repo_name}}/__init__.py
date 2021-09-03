import pkg_resources

__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"
__credits__ = "{{ cookiecutter.credits }}"

__version__ = pkg_resources.require(__package__)[0].version
