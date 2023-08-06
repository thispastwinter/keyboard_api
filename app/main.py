from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.routers.keyboard_router import keyboards_router
from app.routers.keycap_router import keycaps_router
from app.routers.switch_router import switches_router

origins = [
    "http://localhost:3000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def app_docs_redirect():
    return RedirectResponse(url="/api/v1/docs")


app.include_router(keyboards_router)
app.include_router(keycaps_router)
app.include_router(switches_router)

app.mount(path="/api/v1", app=app)
