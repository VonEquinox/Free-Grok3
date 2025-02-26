from flask import Flask, request, jsonify
import answer_program

app = Flask(__name__)

@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    print(1)
    try:
        data = request.get_json()
        messages = data['messages']
        user_message = messages[-1]
        question = user_message['content']
        model = data['model']

        print(f"User question: {question}---Model: {model}")

        answer = answer_program.answer_question(question, model)

        print(f"AI Answer: {answer}")

        response_data = {
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": answer
                    }
                }
            ]
        }
        
        return jsonify(response_data)
    except Exception as e:
        print("------------------------------------------------------------------")
        print(e) 
        print("------------------------------------------------------------------")
        return jsonify({"error": "An error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="::")