# noupoi.net

Personal [noupoi.net](https://www.noupoi.net) website built using [Pelican](https://docs.getpelican.com/en/stable/).

## Setup

Create venv
```
python -m venv ./venv
```

Load venv (PowerShell)
```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
venv\Scripts\Activate.ps1
```

Install dependencies
```
pip install pelican[Markdown] invoke

git clone https://github.com/petrnohejl/MinimalXY.git
pelican-themes --install "<path_to_repo>\MinimalXY" --verbose
```

Build
```
pelican content
```

Test locally
```
pelican --listen
```
