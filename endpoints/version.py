from fastapi import APIRouter


def get_version_router(settings):
    router = APIRouter()

    @router.post("/version")
    async def version():
        return {"version": settings.version}

    return router
