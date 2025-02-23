from flask import Flask, request, jsonify
import answer_program  # 导入你的本地问答程序

app = Flask(__name__)

@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    try:
        data = request.get_json()
        messages = data['messages']
        user_message = messages[-1]
        question = user_message['content']
        answer = answer_program.answer_question(question)
        model = data['model']
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
    except:
        return jsonify({"error": "An error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)