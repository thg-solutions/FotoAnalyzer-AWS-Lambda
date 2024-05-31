## Repository
Probehalber public, aber noch nicht auf "Herz und Nieren" getestet.

## Swagger-UI
http://localhost:8000/docs

## POST Example
```
curl -X 'POST' \
  'http://127.0.0.1:8000/analyze_image' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@PHOTO0007.JPG;type=image/jpeg'
```
oder kürzer:
```
curl http://127.0.0.1:8000/analyze_image \
-F file=@/home/tom/Bilder/PhotoAlbum/PHOTO0007.JPG
```
