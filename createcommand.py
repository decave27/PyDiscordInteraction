import requests

app_id = 123
guild_id = 123
bot_token = "대충 토큰"

commands = [
			    {
					"name": "샌즈",  # 디스코드 힌트 에서 보일 이름
					"value": "sans"  # 시스템에서 보일 이름
				},
				{
					"name": "와!",
					"value": "wa"
				},
                {
					"name": "임베드",
					"value": "embed"
				},
                {
                    "name": "핑",
                    "value": "ping"
                },
                {
                    "name": "존경",
                    "value": "sirjohn"
                }
]

data = {
	"name": "미니봇",
	"description": "미니봇 커맨드들",
	"options": [
		{
			"type": 3,
			"name": "Command",
			"description": "Choose Command",
			"required": True,
			"choices": commands
		},
		{
			"type": 3,
			"name": "text",
			"description": "문자열"
		},
        {
            "type": 4,
            "name": "int",
            "description": "숫자"
        },
		{
			"type": 5,
			"name": "bool",
			"description": "부울"
		},
        {
            "type": 6,
            "name": "user",
            "description": "유저"
        },
		{
			"type": 7,
			"name": "channel",
			"description": "채널"
		},
        {
            "type": 8,
            "name": "role",
            "description": "역할"
        },

	]
}

headers = {
    "Authorization": f"Bot {bot_token}"
}

requests.post(f'https://discord.com/api/v8/applications/{app_id}/guilds/{guild_id}/commands', headers=headers, json=data)