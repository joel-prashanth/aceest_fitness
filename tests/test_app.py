from aceest_fitness import app, workouts
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Home page should load successfully"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Add Workout" in response.data


def test_add_workout(client):
    """Adding a workout should store it in memory"""
    workouts.clear()  # reset before test
    response = client.post("/add_workout", data={
        "workout": "Push Ups",
        "duration": "15",
        "reps": "30",
        "calories": "100"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert any(w["workout"] == "Push Ups" for w in workouts)


def test_view_workouts(client):
    """Workouts page should list added workouts"""
    workouts.clear()
    workouts.append({
        "workout": "Squats",
        "duration": 20,
        "reps": 50,
        "calories": 150,
        "date": "2025-09-01 10:00"
    })

    response = client.get("/workouts")
    assert response.status_code == 200
    assert b"Squats" in response.data


def test_reset_workouts(client):
    """Reset should clear all workouts"""
    workouts.append({
        "workout": "Running",
        "duration": 30,
        "reps": None,
        "calories": 200,
        "date": "2025-09-01 10:30"
    })

    response = client.post("/reset", follow_redirects=True)
    assert response.status_code == 200
    assert len(workouts) == 0
    assert b"All workouts have been reset!" in response.data

# def test_force_fail():
#     assert False, "Intentional failure to test pre-commit"
