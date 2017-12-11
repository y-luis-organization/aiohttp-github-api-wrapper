# GitHub API wrapper

Prerequisites:
-------------
aiohttp

requests

trafaret-config

sqlalchemy

Endpoints
-------------
    GET organizations/

Number of organizations that are at this time in github (according to https://stackoverflow.com/a/47503662/3286487).

    GET organizations/organization_name

Number of repositories and the biggest repository for a given organization name

Both endpoints returns a JSON response.

Tested with:
-------------
trafaret-config 1.0.1

aiohttp 2.3.6

requests 2.10

sqlalchemy 1.1.15