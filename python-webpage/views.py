from flask import Blueprint, render_template, request, jsonify

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", variable1="Adrian", edad=24)

@views.route("/profile")
def profile():
    args = request.args
    variable1 = args.get('nombre')
    return render_template("index.html", variable1 = variable1, edad=24)

# como devoler un json??
@views.route("/json")
def get_json():
    return jsonify({'name': 'Samuel', 'edad':24})