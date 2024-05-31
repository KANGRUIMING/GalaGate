from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# 允许跨域请求
CORS(app)

# 预设的用户信息，包括邮箱、抽奖号码以及是否中奖
users = {
    'user1@example.com': {'lottery_number': 123, 'won': 'yes'},
    'user2@example.com': {'lottery_number': 456, 'won': 'no'},
    'user3@example.com': {'lottery_number': 1, 'won': 'no'},
    'user4@example.com': {'lottery_number': 2, 'won': 'no'},
    'user5@example.com': {'lottery_number': 3, 'won': 'no'},
    'user6@example.com': {'lottery_number': 4, 'won': 'no'},
    'user7@example.com': {'lottery_number': 5, 'won': 'no'},
}

@app.route('/api/checkin', methods=['POST'])
def checkin():
    # Parse the incoming JSON request to extract the email
    # 解析传入的JSON请求以提取邮箱
    data = request.json
    email = data.get('email')

    # Search for the email in the dictionary
    # 在字典中搜索该邮箱
    if email in users:
        user_data = users[email]
        exist = True
        lottery_number = user_data['lottery_number']
        won = user_data['won']
    else:
        exist = False
        lottery_number = -1  # Using -1 to indicate not found or not applicable
        # 使用-1表示未找到或不适用
        won = 'not applicable'

    # Respond with the data
    # 返回查询结果
    return jsonify({
        'exist': exist,
        'lottery_number': lottery_number,
        'won': won
    })

@app.route('/api/lottery-numbers', methods=['GET'])
def get_lottery_numbers():
    # Extract lottery numbers excluding those with a won value of 'yes'
    # 提取未中奖的抽奖号码
    lottery_numbers = [user['lottery_number'] for user in users.values() if user['won'] != 'yes']

    # Return the list of lottery numbers
    # 返回抽奖号码列表
    return jsonify(lottery_numbers)

@app.route('/api/save-numbers', methods=['POST'])
def save_numbers():
    data = request.json
    numbers = data.get('numbers')
    # Logic to save numbers, e.g., store them in a database or a file
    # 保存号码的逻辑，例如将其存储在数据库或文件中
    print(numbers)  # Just for debugging, replace with your actual saving logic
    # 仅用于调试，替换为实际的保存逻辑
    return jsonify({'success': True, 'message': 'Numbers saved successfully'})

# debug=True to avoid restart the local development server manually after each change to your code.
# host='0.0.0.0' to make the server publicly available.
# debug=True 用于在本地开发时避免每次更改代码后手动重启服务器
# host='0.0.0.0' 用于使服务器对外部可访问
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
