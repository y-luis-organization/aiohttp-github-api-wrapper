from aiohttp import web
import db
from organizations import encoders
from organizations.services import get_repos, get_organizations


async def organizations(request):
    organization_name = request.match_info.get('organization', None)

    if organization_name:
        # If organization name parameter is in the request, search whether it is in database
        organization = db.get_organization(request.app['session'], organization_name)

        if organization is None:
            # If not in database, request the API
            response = get_repos(organization_name)
            # And save it for later requests
            db.save_organization(request.app['session'], organization_name, response)
        else:
            # Organization is in database
            response = encoders.encode(organization)

    else:
        response = get_organizations()

    return web.json_response(response)
