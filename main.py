import requests
import urllib.parse
import pyperclip

def get_user_id(slug):
    api_url = f"https://afdian.com/api/user/get-profile-by-slug?url_slug={slug}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        if data.get("ec") == 200 and data.get("data"):
            return data["data"]["user"]["user_id"]
        else:
            print(f"Error from API: {data.get('em', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def build_sponsor_url(user_id, remark):
    return f"https://afdian.com/order/create?user_id={user_id}&remark={urllib.parse.quote(remark)}"

def main():
    slug_input = input("Please input your afdian user name: ")
    if slug_input == "":
        print("user name can't be empty")
        return
    user_id = get_user_id(slug_input)
    if user_id:
        print(f"Successfully fetched User ID: {user_id}")
        remark_input = input("Please input your remark: ")
        sponsor_url = build_sponsor_url(user_id, remark_input)
        pyperclip.copy(sponsor_url)
        print("\nYour sponsor url has been copied to the clipboard:")
        print(sponsor_url)

if __name__ == "__main__":
    main()
