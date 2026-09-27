from flask import Flask, render_template, request, jsonify
from agent import run_agent

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = (data.get("question") or "").strip()

    if not question:
        return jsonify({"answer": "Please enter a question."}), 400

    try:
        result = run_agent(question)
        return jsonify({"answer": result})
    except Exception as e:
        return jsonify({"answer": f"Agent error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
