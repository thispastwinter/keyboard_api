from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.routers.keyboards import keyboards_router

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

app.mount(path="/api/v1", app=app)
