import os

from mangum import Mangum
from asgi_s3.middleware import S3StorageMiddleware, s3_url_for
from starlette.applications import Starlette
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
app = Starlette(debug=True)


def get_request_context(request) -> dict:
    return {"request": request, "s3_url_for": s3_url_for}


@app.route("/")
async def homepage(request):
    template = "index.html"
    context = get_request_context(request)
    return templates.TemplateResponse(template, context)


@app.route("/error")
async def error(request):
    """
    An example error.
    Switch the `debug` setting to see either tracebacks or 500 pages.
    """
    raise RuntimeError("Oh no")


@app.exception_handler(404)
async def not_found(request, exc):
    """
    Return an HTTP 404 page.
    """
    template = "404.html"
    context = get_request_context(request)
    return templates.TemplateResponse(template, context, status_code=404)


@app.exception_handler(500)
async def server_error(request, exc):
    """
    Return an HTTP 500 page.
    """
    template = "500.html"
    context = get_request_context(request)
    return templates.TemplateResponse(template, context, status_code=500)


BUCKET_NAME = os.environ.get("BUCKET_NAME", None)
REGION_NAME = os.environ.get("REGION_NAME", None)

app.add_middleware(
    S3StorageMiddleware,
    bucket_name=BUCKET_NAME,
    region_name=REGION_NAME,
    static_dir="static",
)
handler = Mangum(app)
