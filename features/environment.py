# features/environment.py
import os
import importlib.util


def before_all(context):
    context.headers = {
        "Content-Type": "application/json",
        "x-api-key": "reqres-free-v1"
    }
    steps_dir = os.path.join(os.path.dirname(__file__), "steps")
    for root, _, files in os.walk(steps_dir):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                spec = importlib.util.spec_from_file_location(
                    f"features.steps.{file[:-3]}",
                    os.path.join(root, file)
                )
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)


def before_feature(context, feature):
    # if "resources" in feature.tags:
    #     context.base_url = "https://reqres.in/api"
    #     print(f"🎯 Base URL set for Resources API: {context.base_url}")
    context.base_url = "https://reqres.in/api"
    print(f"🎯 Base URL set for Resources API: {context.base_url}")

    if "single_resources" in feature.tags:
        context.single_resource_endpoint = "/unknown/2"