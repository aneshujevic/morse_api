import jwt

from morse_code import MorseCode
import requests


AUTH_API_URL = "http://omega-morse-service.eu-central-1.elasticbeanstalk.com/api/v1/auth"
RESULT_API_URL = "http://omega-morse-service.eu-central-1.elasticbeanstalk.com/api/v1/result"


def sign_in(username, password):
    data = {'username': username, 'password': password}
    return requests.request('POST', AUTH_API_URL, json=data)


def post_results(first_name, last_name, email, result, github_url, token):
    data = {
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'result': result,
        'githubUrl': github_url
    }
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    return requests.request('POST', RESULT_API_URL, headers=headers, json=data)


if __name__ == '__main__':
    response = sign_in("omega", "candidate")
    if response.status_code != requests.codes.ok:
        print("ERROR SIGNING IN:")
        print(response.text)
        exit(-1)

    jwt_token = response.json()["value"]
    jwt_decoded = jwt.decode(jwt=jwt_token, options={"verify_signature": False})
    exp_date = jwt_decoded['exp']
    text_to_encode = f"Vega IT Omega : {exp_date}"
    encoded_text = MorseCode.encode(text_to_encode)
    results_resp = post_results("Anes", "Hujevic", "anes1996_h@hotmail.com", encoded_text, "https://github.com/aneshujevic/morse_api", jwt_token)
    print(results_resp.text, results_resp.status_code)
