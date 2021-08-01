import os
import sqlite3
import pandas as pd
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from application import app, db
from application.models import World, Continents, Countries


@app.route("/")
@app.route("/home")
def home():
    worlds = World.query.all()
    continents = Continents.query.all()
    countries = Countries.query.all()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "site.db")
    with sqlite3.connect(db_path) as db:

        cursor = db.cursor()
        cursor.execute("SELECT critical_active_percentage FROM world")
        critical_active_percentage = cursor.fetchone()
        cursor.execute(
            "SELECT non_critical_active_percentage FROM world")
        non_critical_active_percentage = cursor.fetchone()
        cursor.execute(
            "SELECT total_deaths_percentage FROM world")
        total_deaths_percentage = cursor.fetchone()
        cursor.execute(
            "SELECT total_recovered_percentage FROM world")
        total_recovered_percentage = cursor.fetchone()

    labels = ["Critical",
              "Non-Critical", "Deaths", "Recovered"]

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "site.db")
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT continent FROM continents")
        continent_names = cursor.fetchall()

        cursor.execute(
            "SELECT critical_active_percentage FROM continents")
        cap = cursor.fetchall()
        cursor.execute(
            "SELECT non_critical_active_percentage FROM continents")
        ncap = cursor.fetchall()

        cursor.execute(
            "SELECT total_deaths_percentage FROM continents")
        tdp = cursor.fetchall()

        cursor.execute(
            "SELECT total_recovered_percentage FROM continents")
        trp = cursor.fetchall()

        cursor.execute(
            "SELECT date_processed FROM continents")
        dp = cursor.fetchall()

        cursor.execute(
            "SELECT total_deaths FROM continents")
        td = cursor.fetchall()

        cursor.execute(
            "SELECT critical_active FROM continents")
        ca = cursor.fetchall()

        cursor.execute(
            "SELECT non_critical_active FROM continents")
        nca = cursor.fetchall()

        cursor.execute(
            "SELECT total_recovered FROM continents")
        tr = cursor.fetchall()

        continents_data = []
        i = 0

        for continent_name in continent_names:
            ls = [continent_name[0], cap[i][0], ncap[i][0], tdp[i][0],
                  trp[i][0], dp[i][0], td[i][0], ca[i][0], nca[i][0], tr[i][0]]
            i += 1
            continents_data.append(ls)

    # Detect the current page
    segment = get_segment(request)

    return render_template('home.html', segment=segment, worlds=worlds, continents=continents, continents_data=continents_data, countries=countries, labels=labels, critical_active_percentage=critical_active_percentage, non_critical_active_percentage=non_critical_active_percentage, total_deaths_percentage=total_deaths_percentage, total_recovered_percentage=total_recovered_percentage)


@ app.route("/about")
def about():
    return render_template('about.html', title='About')


@ app.route("/world/<int:index>")
def world(index):
    world = World.query.get_or_404(index)
    return render_template('world.html', world=world)


@ app.route("/continent/<int:index>")
def continent(index):
    continent = Continents.query.get_or_404(index)
    return render_template('continent.html', continent=continent)


@ app.route("/country/<int:index>")
def country(index):
    country = Countries.query.get_or_404(index)
    return render_template('country.html', country=country)


@ app.route("/test")
def test():
    return render_template('layout2.html')

# Helper - Extract current page name from request


def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
