import click 
from models import User, Activity, Meal, HealthMetric, create_engine, session


@click.group()
def cli():
    pass

@cli.command()
@click.option("--username", prompt="Enter Username")
def register_user(username):
    print("Printing username=========")
    print(username)
    user = User(username=username)
    print(user)
    session.add(user)
    session.commit()
    click.echo(f'User {username} registered successfully.')

@cli.command()
@click.option('--username', prompt="Enter username")
def add_activity(username):
    # user= click.prompt("Enter username: ")
    user = session.query(User).filter_by(username=username).first()
    if user:
        activity_type = click.prompt('Activity Type')
        duration_minutes = click.prompt('Duration (minutes)', type=int)
        activity = Activity(user=user, activity_type=activity_type, duration_minutes=duration_minutes)
        session.add(activity)
        session.commit()
        click.echo(f'Activity {activity_type} added successfully.')
    else:
        click.echo(f'User {username} not found.')

@cli.command()
@click.option('--username', prompt="Enter Username")
def add_meal(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        food_items = click.prompt('Meal')
        nutritional_info = click.prompt('Nutritional Information')
        meal = Meal(user=user, food_items=food_items, nutritional_info=nutritional_info)
        session.add(meal)
        session.commit()
        click.echo('Meal added successfully.')
    else:
        click.echo(f'User {username} not found.')

@cli.command()
@click.option('--username', prompt="Enter Username")
def add_health_metric(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        weight_kg = click.prompt('Weight (kg)', type=float)
        sleep_duration_hours = click.prompt('Sleep Duration (hours)', type=float)
        health_metric = HealthMetric(user=user, weight_kg=weight_kg, sleep_duration_hours=sleep_duration_hours)
        session.add(health_metric)
        session.commit()
        click.echo('Health metric added successfully.')
    else:
        click.echo(f'User {username} not found.')

@cli.command()
@click.option('--username', prompt="Enter Username")
def view_summary(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        activities = user.activities
        meals = user.meals
        health_metrics = user.health_metrics

        click.echo('--- Daily Summary ---')
        click.echo(f'Activities: {activities}')
        click.echo(f'Meals: {meals}')
        click.echo(f'Health Metrics: {health_metrics}')

    
    else:
        click.echo(f'User {username} not found.')

if __name__ == '__main__':
    cli()