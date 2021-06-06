# wrappy
A simple api wrapper for any api.

## Usage: 
import Wrapper from main

> i = Wrapper(base="http://localhost/", headers={"Auth":"auth_token"})
> #example request:
> res = i.get("images", params={"length":5})
> print(res.status_code)
> print(res.json())
