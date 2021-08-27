# CY-Filter-API
Flask-Python-MongoDB based Youtube Cyberbully Comment Filter RESTful API

```
[ENDPOINT] /api/
[GET] /api/get_detail=<videoid> - Fetch Unprocessed Youtube Comments from a Video
[GET] /api/get_comment=<videoid>&max_result=<max_result>&search_term=<search_term> - Fetch unprocessed Youtube Comments from a Video with max_result & search_term parameters
[GET] /api/get_comment=<videoid>&max_result=<max_result> - Fetch unprocessed Youtube Comments from a Video with max_result parameter
