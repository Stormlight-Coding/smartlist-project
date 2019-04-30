from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
import bcrypt
import os
# import PIL import Image
from googleapiclient.discovery import build
from models import *
# from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
test_user_id = 1
DEVELOPER_KEY = "AIzaSyBgG7A9CLr86yVRwSeNRM_GvoBCUV19MuQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def index(request):
    return render(request,'smartlist_app/index.html')

def login(request):
    return redirect("/dashboard")

def register(request):
    return redirect("/dashboard")

def dashboard(request):
    todos = Todo.objects.filter(created_by=test_user_id, done=False)
    context = {
        "todos":todos,
    }
    return render(request,'smartlist_app/dashboard.html', context)

def add_todo(request):
    request.session["query"] = request.POST["query"]
    user_id = User.objects.get(id=1)
    todo = Todo.objects.create(name=request.session["query"], created_by=user_id)
    resources = main(request)
    videos = youtube_search(request)
    print videos
    title = []
    img = []
    link= []
    l = 0
    while l < len(videos["items"]):
      img.append(videos["items"][l]["snippet"]["thumbnails"]["default"]["url"])
      title.append(videos["items"][l]["snippet"]["title"])
      link.append(videos["items"][l]["id"]["videoId"])
      l = l + 1
    for i in range(0,6):
        Video.objects.create(title= title[i], link=link[i], snippet= img[i], video_owner=todo)
    for r in resources:
        Resource.objects.create(title=r["title"], link=r["link"], snippet= r["snippet"], resource_owner=todo)
        # print r
    return redirect("/dashboard")

def youtube_search(request):
    res = []
    if "query" in request.session:
      youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)
      search_response = youtube.search().list(
        q="how to" + request.session["query"],
        part="id,snippet",
        maxResults= 6
      ).execute()
    #   if __name__ == "__main__":
    #       argparser.add_argument("--q", help="Search term", default="Google")
    #       argparser.add_argument("--max-results", help="Max results", default=25)
    #       args = argparser.parse_args()
      #
    #   try:
    #     youtube_search(args)
    #   except HttpError, e:
    #     print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
      return search_response
    else:
      return res



def main(request):
    #build the the service url
    res = []
    if "query" in request.session:
        service = build("customsearch", "v1",
                developerKey="AIzaSyAR8ys4lyNRUgoPbqQpycajlv1j4PiOGPk")

        res = service.cse().list(

          q="how to" + request.session["query"],
          cx="005614876608685890370:czwekc7ki7q",
        ).execute()
        return res["items"]
    else:
        return res

def delete_todo(request,id):
    Todo.objects.get(id=id).delete()
    return redirect("/dashboard")

def delete_resource(request,id):
    Resource.objects.get(id=id).delete()
    return redirect("/dashboard")

def history(request):
    todos = Todo.objects.filter(created_by=test_user_id, done=True)
    context = {
        "todos":todos,
    }
    return render(request,'smartlist_app/history.html', context)

def registration(request):
    return render(request,'smartlist_app/registration.html')

def clean_history(request):
    todos = Todo.objects.filter(created_by=test_user_id).filter(done=True).delete()
    return redirect("/history")

def todo_done(request, id):
    Todo.objects.filter(id=id).update(done = True)
    return redirect("/dashboard")
