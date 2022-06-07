from django.shortcuts import render
from .models import Users_login,User_post,Post_vote
from django.http import HttpResponse, Http404,FileResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
#For user Profile login page 
def voting(request,id):
    if Users_login.objects.filter(id=id).exists():
        userIDp=Users_login.objects.get(id=id)
        post_list= Post_vote.objects.all()
        allPostdata=User_post.objects.filter(user_Id=id)
        mainlist=[post_list,allPostdata]

        return render(request,'userLogin.html',{'context':post_list,'id':userIDp.id,'allPostdata':allPostdata})
    else:
        return HttpResponse("User not Created")


#For Counting upvoting and downvoting with saving data in dbs with respected user and post
@csrf_exempt
def upvotedata1(request,userid,postid):
    data1= request.POST.get('up_votedata')
    data2= request.POST.get('down_votedata')
    print('data1',data1)
    if request.POST.get('up_votedata'):
        if User_post.objects.filter(postID=postid,user_Id=userid).exists():
            userPost=User_post.objects.get(postID=postid,user_Id=userid)
            userPost.upvote_User=data1
            userPost.save()
        else:
            if User_post.objects.filter(postID=postid,user_Id=userid).exists():
                down_user=User_post.objects.get(postID=postid,user_Id=userid)
                down_user1=down_user.downvote_User
            else:
                down_user1=0

            User_post.objects.create(postID=postid,user_Id=userid,upvote_User=data1,downvote_User=down_user1)
    if request.POST.get('down_votedata'):
        if User_post.objects.filter(postID=postid,user_Id=userid).exists():
            userPost=User_post.objects.get(postID=postid,user_Id=userid)
            userPost.downvote_User=data2
            userPost.save()
        else:
            if User_post.objects.filter(postID=postid,user_Id=userid).exists():
                up_user=User_post.objects.get(postID=postid,user_Id=userid)
                up_user1=up_user.upvote_User
            else:
                up_user1=0

            
            User_post.objects.create(postID=postid,user_Id=userid,upvote_User=up_user1,downvote_User=data2)

    return JsonResponse("ok",safe=False)
#for shoving previous voted data on user login profile
@csrf_exempt
def olddata(request,userid):
    oldDatapostlist=[]
    oldDatapostlist1=[]
    oldDatapost=User_post.objects.filter(user_Id=userid)
    for i in oldDatapost:
        oldDatapostlist.append([i.postID,i.upvote_User,i.downvote_User])
        #oldDatapostlist1.append(i.postID)
    return JsonResponse(oldDatapostlist,safe=False)

#for creating user and post
def dbl(request):
    # Users_login.objects.create(userName='vicky')
    # Users_login.objects.create(userName='ajay')
   # Users_login.objects.create(userName='vicky')
    # Users_login.objects.all().delete()
    # User_post.objects.all().delete()
    # Users_login.objects.create(userName='summet')
    # Post_vote.objects.filter(postName='votingPost1').delete()
    # Post_vote.objects.filter(postName='votingPost2').delete()
    Post_vote.objects.create(postName='Post3')
    Post_vote.objects.create(postName='Post4')
    Post_vote.objects.create(postName='Post5')
    Post_vote.objects.create(postName='Post6')

   
    return HttpResponse("request successful")