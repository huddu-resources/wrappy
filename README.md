# wrappy
A simple api wrapper for any api.

## Usage: 
import Wrapper from main

> i = Wrapper(base="http://localhost/", headers={"Auth":"auth_token"})<br>
> #example request:<br>
> res = i.get("images", params={"length":5})<br>
> print(res.status_code)<br>
> print(res.json())<br>
