from fastapi import FastAPI
from pydantic import BaseModel
from runsolution import run_solution_to_check


class Exercise(BaseModel):
    name: str
    description: str | None = None
    solution: str | None = None

app = FastAPI()


@app.post("/")
async def create_exercise(exercise: Exercise):
    print(exercise)
    name = exercise.name
    description = exercise.description
    solution = exercise.solution
    result = run_solution_to_check(name, description, solution)
    print(result)
    return {"result": result}

