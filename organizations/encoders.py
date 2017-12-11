def encode(organization):
    """
    Enconde an Organization instance to a dictionary
    :param organization:
    :return:
    """
    return {'public_repos': organization.public_repos,
            'biggest_repo': {'size': organization.biggest_repo_size, 'name': organization.biggest_repo_name}}
