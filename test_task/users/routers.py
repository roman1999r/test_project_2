from rest_framework import routers


class MyRouter(routers.SimpleRouter):
    routers = [
        routers.Route(
            url=r'^{prefix}$',
            mapping={'post': 'create'},
            name='{basename}-create',
            detail=False,
            initkwargs={'suffix': 'Create'}
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        routers.Route(
            url=r'user-list',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'Detail'}
        ),
    ]

