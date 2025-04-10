from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("""
<!DOCTYPE html>
<html>
<head>
    <title>VN Technosoft Backend</title>
</head>
<body style='font-family: sans-serif; background-color: #f0f8ff; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0;'>
    <div style='text-align: center;'>
        <h1 style='font-size: 2.5rem;'>🎉 Welcome to <span style='color: #007bff;'>VN Technosoft Backend</span> 🎯</h1>
        <p style='font-size: 1.2rem;'>🚀 This Django app is running on <strong style='color: green;'>Render</strong>!</p>
    </div>
</body>
</html>
""", content_type="text/html")

urlpatterns = [
    path('', home),
]
