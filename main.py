from flask import Flask, jsonify, request
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
from requests import post

pub = '대충 퍼블릭키'

verify = VerifyKey(pub, encoder=HexEncoder)

def check(sign, msg):
    try:
        verify.verify(msg, HexEncoder.decode(sign))
        return True
    except BadSignatureError:
        return False

app = Flask(__name__)

@app.route('/', methods=['POST'])
def Interaction():
    if request.json["type"] == 1:
        sign = request.headers['x-signature-ed25519'].encode()
        time = request.headers['x-signature-timestamp']
        body = request.data

        msg = time.encode() + body

        if check(sign, msg):
            return jsonify({
                "type": 1
            })
        else:
            return jsonify({'result': False}), 400

    elif request.json['type'] == 2:
        data = request.json

        content = ""
        
        cmd = data['data']['options'][0]['value']

        def getArg(argname):
            for i in data['data']['options']:
                if i['name'] == argname:
                    return i['value']

        guild_id = data['guild_id']
        channel_id = data['channel_id']
        user = data['member']['user']
        user_name = user['username']
        user_id = user['id']

        if cmd == "sans":
            content = "아시는구나!"
        
        if cmd == "wa":
            if not getArg('text'):
                return jsonify({
                    "type": 4,
                    "data": {
                        "content": "text arg 필요!"
                    }
                })
            
            content = f"와! {getArg('text')}"
        
        if cmd == "embed":
            return jsonify({
                "type": 4,
                "data": {
                    "embeds": [
                        {
                            "title": "멋진 임베드",
                            "description": "슬래시 커맨드는 버그가 많아요..",
                            "color": 0xFF0000
                        }
                    ]
                }
            })
        
        if cmd == "ping":
            content = f"<@!{user_id}> 퐁!"
        
        if cmd == "sirjohn":
            sj = f"<@!{user_id}>"
            if getArg('user'):
                sj = f"<@!{getArg('user')}>"

            content = f"{sj} 님 존경"
            
        return jsonify({
            "type": 4,
            "data": {
                "content": content
            }
        })

app.run('0.0.0.0', 80, True)