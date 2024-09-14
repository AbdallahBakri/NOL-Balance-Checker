import requests
import re
while True:
    nol_tag_id = input("Enter the NOL number: ").strip()
    if nol_tag_id.isdigit() and len(nol_tag_id) >= 10:  
        break
    else:
        print("Invalid NOL number. Please enter a valid NOL number.")
data = {
    'nolTagId': nol_tag_id,
    'g-recaptcha-response': '03AFcWeA7NAEbhLtvyDa53ZpwezKXmsXAMFejXQ8kd-6rSLqUMq5xs035_Zrkrs0HOnY0vMLCHhkNkYUWJIiEPlxGcCtJaorWa-hiiBSDGqz-DSK48kQyUeNK5XrIpHnrRJ_C3tJ0muTONWSJPuG1ni3v35eu1e-8OjPtK0jKWvlX35ihoUYsTDq3axD-Vzwi6_-kBIlh11ZpjGQAQN-y8_Leipk_8t5gXyNvgal1v6wTAgQ8V-7_rCk_yuidAe08rFmnjHxw9G1jTn454LPwWftmMcCjqBA3BtDnyPQvZZhudOHYGBshrqB3si4SKeGs95CECyRfyU9MXO45pQk_4qpJ2LJyWXzRtbZNeYz7qBu0iJEpIyfm5NvlyDiGp27EaZ6mAT35pxIXIJLWhXCJosNq9GDAkTlpt25upLZTME9slVfK92ME1dvyDEFpjEuzAWGkudNB_ohrY6J0FBL0jCPtQRmdVbWMuxJsCbQD0COvRWfleJMuFsuTBThU6YH94NW1u0PRKyE2iiKaKxDxoANp5J3F0kZOq3mMIup54VMCa8q4sLLo38jsAdNPH6oJge5OQmVDEZUOeJijAu3jNqOmzOGBHlhyUPfqjcmHsWI6BMwIYvK9pxRNAdVBrFYH93zRpCyMdC9d1ja_vJlZYNt4-UkDOc1l_u16-Zn0SZQPELR6f6ioh0MnzNeWWsU5fRtAGZgYBdKpm3sjKDX_lbW6PY77eT_DlPyvbhOrI9UqSM_WbMBAOGTXuE5BbwfK4NlZZLUL5Bnag1AOTKcHzvv-MKDFR4-LgLFQWItLJdrijKpzPgMvLc-YYONmzu5uTBaGQTEpkSZXtWlpXHxkMru8t3LeLOLaDwA',
    'captchaResponse': '03AFcWeA7NAEbhLtvyDa53ZpwezKXmsXAMFejXQ8kd-6rSLqUMq5xs035_Zrkrs0HOnY0vMLCHhkNkYUWJIiEPlxGcCtJaorWa-hiiBSDGqz-DSK48kQyUeNK5XrIpHnrRJ_C3tJ0muTONWSJPuG1ni3v35eu1e-8OjPtK0jKWvlX35ihoUYsTDq3axD-Vzwi6_-kBIlh11ZpjGQAQN-y8_Leipk_8t5gXyNvgal1v6wTAgQ8V-7_rCk_yuidAe08rFmnjHxw9G1jTn454LPwWftmMcCjqBA3BtDnyPQvZZhudOHYGBshrqB3si4SKeGs95CECyRfyU9MXO45pQk_4qpJ2LJyWXzRtbZNeYz7qBu0iJEpIyfm5NvlyDiGp27EaZ6mAT35pxIXIJLWhXCJosNq9GDAkTlpt25upLZTME9slVfK92ME1dvyDEFpjEuzAWGkudNB_ohrY6J0FBL0jCPtQRmdVbWMuxJsCbQD0COvRWfleJMuFsuTBThU6YH94NW1u0PRKyE2iiKaKxDxoANp5J3F0kZOq3mMIup54VMCa8q4sLLo38jsAdNPH6oJge5OQmVDEZUOeJijAu3jNqOmzOGBHlhyUPfqjcmHsWI6BMwIYvK9pxRNAdVBrFYH93zRpCyMdC9d1ja_vJlZYNt4-UkDOc1l_u16-Zn0SZQPELR6f6ioh0MnzNeWWsU5fRtAGZgYBdKpm3sjKDX_lbW6PY77eT_DlPyvbhOrI9UqSM_WbMBAOGTXuE5BbwfK4NlZZLUL5Bnag1AOTKcHzvv-MKDFR4-LgLFQWItLJdrijKpzPgMvLc-YYONmzu5uTBaGQTEpkSZXtWlpXHxkMru8t3LeLOLaDwA'
}
try:
    response = requests.post(
        'https://www.rta.ae/wps/portal/rta/ae/home/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi_QwMTNwNTAx93EPNDAwcQ4MCA8O8gowNXMz1w_Wj9KNASgIMLTycDAx9DIxDnIBKAkO8Ai29PD0MjaEKDHAARwP94NQ8_YLs7DRHR0VFAE1hpMw!/p0/IZ7_KG402B82MGIF8066PQMJDP1OK2=CZ6_N004G041LGU600AURQQVJR30D7=NJgetNolCardBalance=/',
        data=data
    )
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error during the request: {e}")
    exit()
html_content = response.text
balance_pattern = re.compile(r'Your balance is:\s*<br/><strong class="font-weight-bolder font-size-18">([\d.]+)</strong> AED')
pending_credit_pattern = re.compile(r'Pending credit:\s*<br/><strong class="font-weight-bolder font-size-18">([\d.]+)</strong> AED')
expiry_date_pattern = re.compile(r'Expiry date:\s*<br/><strong class="font-weight-bolder font-size-18">([\d/]+)</strong>')
balance = balance_pattern.search(html_content)
pending_credit = pending_credit_pattern.search(html_content)
expiry_date = expiry_date_pattern.search(html_content)
if balance:
    print(f"Balance: {balance.group(1)} AED")
else:
    print("Error during the request: Balance not found.")
if pending_credit:
    print(f"Pending Credit: {pending_credit.group(1)} AED")
else:
    print("Error during the request: Pending Credit not found.")
if expiry_date:
    print(f"Expiry Date: {expiry_date.group(1)}")
else:
    print("Error during the request: Expiry Date not found.")
print("Please note that the shown balance may not include transactions that occurred in the past 48 hours.")
