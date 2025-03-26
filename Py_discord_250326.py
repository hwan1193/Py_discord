import requests
import json

class CompletionExecutor:
    def __init__(self, host, api_key, request_id):
        self._host = host
        self._api_key = api_key
        self._request_id = request_id

    def execute(self, completion_request):
        headers = {
            'Authorization': self._api_key,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'text/event-stream'
        }
        output = ""
        with requests.post(self._host + '/testapp/v1/chat-completions/HCX-003',
                           headers=headers, json=completion_request, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    decoded_line = line.decode("utf-8")
                    print(decoded_line)  # 콘솔 출력
                    output += decoded_line + "\n"
        return output

if __name__ == '__main__':
    # ClovaX API 호출을 위한 CompletionExecutor 객체 생성
    completion_executor = CompletionExecutor(
        host='https://clovastudio.stream.ntruss.com',
        api_key='https://clovastudio.stream.ntruss.com/testapp/v1/chat-completions/HCX-003',
        request_id='71679f35af114ed689fce2d61389ab3e'
    )

    # IT Recruitment 관련 preset 메시지 구성
    preset_text = [
        {"role": "system", "content": ""},
        {"role": "user", "content": "IT 인재 매칭 관련해서 내용 정리 해줘."},
        {"role": "assistant", "content": (
            "IT 인재 매칭은 기업이 필요로 하는 IT 인재와 구직자를 연결해주는 서비스입니다. 다음은 IT 인재 매칭에 대한 내용입니다.\n\n"
            "1. **기업의 요구사항 파악**: 기업은 자사가 필요로 하는 기술과 역량을 가진 인재를 찾기 위해 채용 공고를 게시합니다. "
            "이때, 기업은 자신들이 원하는 인재상과 요구되는 역량 등을 명확하게 제시해야 합니다.\n\n"
            "2. **구직자의 경력 및 역량 분석**: 구인 기업에서 제출한 채용 공고를 바탕으로 해당 분야에서의 경력과 역량을 보유한 후보자들을 선별합니다. "
            "이후 이력서와 포트폴리오 등을 검토하여 최종 후보자를 선정합니다.\n\n"
            "3. **인재 추천**: 전문성을 갖춘 헤드헌터나 컨설턴트가 직접 면접을 진행하거나, 온라인 면접을 지원하기도 합니다. "
            "이를 통해 기업과 구직자 모두에게 적합한 인재를 찾아줍니다.\n\n"
            "4. **채용 후 관리**: 입사 후에도 지속적인 모니터링과 피드백을 제공하여 업무 적응을 돕고, 성과 향상을 지원합니다.\n\n"
            "5. **성과 평가**: 주기적으로 실시하여 보상과 승진 등의 인사 결정에 반영합니다.\n\n"
            "6. **재매칭**: 이직이나 퇴사 등의 이유로 인력 공백이 발생할 경우"
        )},
        {"role": "user", "content": "구직자의 경력 및 역량 분석에 대해 알려줘"},
        {"role": "assistant", "content": (
            "구직자의 경력 및 역량 분석은 IT 인재 매칭에서 매우 중요한 과정 중 하나입니다. 이 과정에서는 다음과 같은 요소들을 고려합니다.\n\n"
            "1. **경력**: 이전 직장에서의 근무 기간, 담당 업무, 프로젝트 경험 등을 파악합니다. 이를 통해 구직자가 해당 분야에서 얼마나 많은 경험을 쌓았는지, "
            "어떤 역할을 수행했는지 파악할 수 있습니다.\n\n"
            "2. **학력**: 전공 분야, 학점, 졸업 여부 등을 파악합니다. 이를 통해 구직자가 해당 분야에서 필요한 지식과 기술을 충분히 습득했는지 판단할 수 있습니다.\n\n"
            "3. **기술 역량**: 보유 기술과 능력을 파악합니다. 예를 들어, 프로그래밍 언어, 데이터베이스, 네트워크 등의 기술을 다룰 수 있는지, "
            "개발 도구를 능숙하게 사용할 수 있는지 파악합니다.\n\n"
            "4. **자격증**: 취득한 자격증을 파악하여 구직자의 전문성을 확인합니다.\n\n"
            "5. **포트폴리오**: 제작한 프로젝트 결과물을 모아 구직자의 역량을 구체적으로 파악합니다.\n\n"
            "6. **자기소개서**: 자신의 경력과 역량을 소개하는 문서로 전반적인 능력을 평가합니다."
        )},
        {"role": "user", "content": "그럼 IT 각 직무들에 대해 소개 좀 해줘"},
        {"role": "assistant", "content": (
            "네. IT 분야에는 다양한 직무들이 존재합니다. 대표적인 IT 직무들은 다음과 같습니다.\n\n"
            "1. **개발자(Developer)**: 소프트웨어를 개발하는 일을 담당하며, 프로그래밍 언어를 이용하여 코드를 작성하고, 시스템을 구축합니다. "
            "웹 개발, 앱 개발, 게임 개발 등 다양한 분야에서 활동합니다.\n\n"
            "2. **데이터 분석가(Data Analyst)**: 데이터를 수집하고 분석하여 기업의 의사결정에 도움을 주는 역할을 담당합니다.\n\n"
            "3. **보안 전문가(Security Expert)**: 컴퓨터 시스템과 네트워크 보안을 담당하며, 해킹 공격을 방어하고 보안 시스템을 구축합니다.\n\n"
            "4. **인공지능(AI) 엔지니어**: AI 기술을 연구하고 개발하며, 머신러닝 및 딥러닝을 활용해 자동화 솔루션을 개발합니다.\n\n"
            "5. **빅데이터(Big Data) 엔지니어**: 대용량 데이터를 처리하고 분석하며, 빅데이터 플랫폼을 구축하고 운영합니다.\n\n"
            "6. **디자인(Design) 직군**: 제품이나 서비스의 디자인, 특히 UI/UX를 담당합니다."
        )}
    ]

    request_data = {
        'messages': preset_text,
        'topP': 0.8,
        'topK': 0,
        'maxTokens': 256,
        'temperature': 0.5,
        'repeatPenalty': 5.0,
        'stopBefore': [],
        'includeAiFilters': True,
        'seed': 0
    }
    
    print(preset_text)
    # ClovaX API 실행 및 출력 캡처
    output = completion_executor.execute(request_data)
    
    # Discord 웹훅 전송 코드
    headers = {
        "Content-Type": "application/json"
    }
    json_data = {
        "embeds": [{
            "title": "[⭐️]이스트소프트_디스코드봇",
            "description": output,
            "url": "https://github.com/dscoool/aisecurity/blob/main/discord_send_msg.py",
            "thumbnail": {
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSx1kkiO_HhVWIXL-RBDOLDzNVjHvcDNxl11swe-mvGzbpHQdYYDzye3_Y&usqp=CAE&s"
            }
        }]
    }
    
    webhook_url = "https://discord.com/api/webhooks/1354326445207457915/1mcS8hAq8BbYPSZ4urJH0Xr3RR6mA6cmBOcsA-K0RMbZz2TKkiwJBgMWeFOkRJyrwToO"
    response = requests.post(webhook_url, headers=headers, json=json_data)
    print("Webhook response:", response.status_code)