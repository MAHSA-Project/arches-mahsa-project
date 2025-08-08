import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"mahsa_project"), "mahsa_project.urls", name="mahsa_project"),
)
