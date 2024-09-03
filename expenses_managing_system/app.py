from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config.Config')

mongo = PyMongo(app)

# Add a new expense to a user's account
@app.route('/api/users/<user_id>/accounts/<account_id>/expenses', methods=['POST'])
def add_expense(user_id, account_id):
    data = request.json
    description = data.get('description')
    amount = data.get('amount')

    if not description or not amount:
        return jsonify({"error": "Missing description or amount"}), 400

    expense = {
        "_id": ObjectId(),
        "description": description,
        "amount": amount,
        "date": datetime.utcnow().strftime('%Y-%m-%d')
    }

    # Find the user and account
    result = mongo.db.users.update_one(
        {"_id": ObjectId(user_id), "accounts._id": ObjectId(account_id)},
        {"$push": {"accounts.$.expenses": expense}}
    )

    if result.matched_count == 0:
        return jsonify({"error": "User or account not found"}), 404

    return jsonify({"message": "Expense added successfully", "expense": expense}), 201

# Get all expenses for a user's account
@app.route('/api/users/<user_id>/accounts/<account_id>/expenses', methods=['GET'])
def get_expenses(user_id, account_id):
    user = mongo.db.users.find_one(
        {"_id": ObjectId(user_id), "accounts._id": ObjectId(account_id)},
        {"accounts.$": 1}
    )

    if not user:
        return jsonify({"error": "User or account not found"}), 404

    account = user['accounts'][0]
    expenses = account.get('expenses', [])

    return jsonify({"account": account_id, "expenses": expenses}), 200

if __name__ == '__main__':
    app.run(debug=True)
