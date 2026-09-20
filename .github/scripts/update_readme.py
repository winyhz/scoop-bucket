import glob
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path


def check_github_repo(owner, repo):
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(api_url, headers={"User-Agent": "Scoop-Bucket-Bot"})
    try:
        urllib.request.urlopen(req)
        return True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False
        return True
    except Exception:
        return True


def main():
    files = sorted(glob.glob("bucket/*.json"))
    rows = []
    dead_apps = []

    for file_path in files:
        data = json.loads(Path(file_path).read_text(encoding="utf-8"))
        name = Path(file_path).stem
        homepage = data.get("homepage", "#")
        version = data.get("version", "N/A")
        desc = data.get("description", "No description provided.").replace("|", "-")

        lic = data.get("license", "Unknown")
        if isinstance(lic, dict):
            lic = lic.get("identifier", "Unknown")

        is_dead = False
        match = re.search(r"github\.com/([^/]+)/([^/]+)", homepage)
        if match:
            owner, repo = match.group(1), match.group(2).replace(".git", "")
            if not check_github_repo(owner, repo):
                is_dead = True
                dead_apps.append((name, homepage))

        if is_dead:
            rows.append(f"| [~~{name}~~]({homepage}) *(⚠️ Upstream 404)* | `{version}` | {desc} | {lic} |")
        else:
            rows.append(f"| [{name}]({homepage}) | `{version}` | {desc} | {lic} |")

    table = "| Application | Version | Description | License |\n| :--- | :--- | :--- | :--- |"
    if rows:
        table += "\n" + "\n".join(rows)

    readme_path = Path("README.md")
    content = readme_path.read_text(encoding="utf-8")
    new_content = re.sub(
        r"<!-- APPLIST:START -->.*?<!-- APPLIST:END -->",
        f"<!-- APPLIST:START -->\n{table}\n<!-- APPLIST:END -->",
        content,
        flags=re.DOTALL,
    )
    readme_path.write_text(new_content, encoding="utf-8")
    print(f"Updated README.md with {len(files)} applications.")

    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file and dead_apps:
        with open(summary_file, "a", encoding="utf-8") as f:
            f.write("## ⚠️ Dead Upstream Warning (已删库警告)\n\n")
            f.write("| App | Homepage | Status |\n| :--- | :--- | :--- |\n")
            for name, url in dead_apps:
                f.write(f"| **{name}** | [{url}]({url}) | 404 Not Found |\n")


if __name__ == "__main__":
    main()
