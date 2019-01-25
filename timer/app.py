from timer.config import settings
from timer.tasks.core import Manager

from sanic import Sanic
from sanic.response import json

task_manager = Manager()
tasks = task_manager.get_tasks()
app = Sanic(log_config=settings.LOGGING)


@app.route("/")
async def test(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, backlog=128)
