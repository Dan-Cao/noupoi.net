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
pip install -r requirements.txt

git clone https://github.com/petrnohejl/MinimalXY.git
pelican-themes --install "<path_to_repo>\MinimalXY" --verbose
```

Build and test
```
invoke reserve
```

Deploy
```
invoke gh-pages
```

## Notes

TypeError when running deployment?
  * https://github.com/getpelican/pelican/issues/2489#issuecomment-472176621