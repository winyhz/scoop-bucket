# 🪣 winyhz's Scoop Bucket

[![Excavator](https://github.com/winyhz/scoop-bucket/actions/workflows/excavator.yml/badge.svg)](https://github.com/winyhz/scoop-bucket/actions/workflows/excavator.yml)
[![License](https://img.shields.io/github/license/winyhz/scoop-bucket?color=blue)](LICENSE)
[![Applications](https://img.shields.io/github/directory-file-count/winyhz/scoop-bucket/bucket?label=apps&color=orange)](bucket)

A personal [Scoop](https://scoop.sh/) bucket maintaining customized, portable, or unofficial manifests that are not available in the official Scoop buckets.

---

## 🚀 Getting Started

### 1. Add this bucket
To add this bucket to your local Scoop installation, run:

```powershell
scoop bucket add winyhz https://github.com/winyhz/scoop-bucket
```

### 2. Install applications
Once the bucket is added, you can install any package using:

```powershell
scoop install winyhz/<app-name>

# Example:
scoop install winyhz/ukmm
```

---

## 📦 Available Applications

The table below is **automatically updated** whenever manifests are added or updated.

<!-- APPLIST:START -->
| Application | Version | Description | License |
| :--- | :--- | :--- | :--- |
| [Switch-Toolbox](https://github.com/KillzXGaming/Switch-Toolbox) | `Final` | A tool to edit and preview many video game file formats from Nintendo Switch, Wii U, and 3DS. | GPL-3.0-or-later |
| [WiiUDownloader](https://github.com/Xpl0itU/WiiUDownloader) | `3.2` | Download Wii U games, updates, DLC, and demos directly from Nintendo's servers, no title keys needed. | GPL-3.0-or-later |
| [qcma](https://codestation.github.io/qcma/) | `0.4.1` | Cross-platform content manager assistant for the PS Vita | GPL-3.0-or-later |
| [ukmm](https://github.com/NiceneNerd/ukmm) | `0.17.1` | U-King Mod Manager is a tool for managing and merging mods for The Legend of Zelda: Breath of the Wild. It should be considered a successor to BCML. | GPL-3.0-or-later |
<!-- APPLIST:END -->

---

## 🔄 Automatic Updates

All manifests in this bucket are monitored and automatically updated using [ScoopInstaller/GithubActions](https://github.com/ScoopInstaller/GithubActions). When upstream repositories release new versions, manifests and checksums are checked, validated, and updated via GitHub Actions.

---

## 📄 License

This repository and all manifest metadata are released under the **[The Unlicense](LICENSE)**.

> **Note**: Software packages and binaries downloaded through these manifests remain subject to their respective original authors' licenses.
