from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/predict")
def predict_page(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request}
    )


@app.post("/predict")
async def predict_datapoint(request: Request):

    form = await request.form()

    data = CustomData(
        gender=form.get("gender"),
        race_ethnicity=form.get("race_ethnicity"),
        parental_level_of_education=form.get("parental_level_of_education"),
        lunch=form.get("lunch"),
        test_preparation_course=form.get("test_preparation_course"),
        reading_score=int(form.get("reading_score")),
        writing_score=int(form.get("writing_score"))
    )

    final_new_data = data.get_data_as_dataframe()

    print(final_new_data)

    predict_pipeline = PredictPipeline()

    result = predict_pipeline.predict(final_new_data)

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "results": result[0]
        }
    )


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )