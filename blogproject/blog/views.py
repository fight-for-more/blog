from django.shortcuts import render
from blog.models import NoteInfo,TagInfo,CommentInfo
from django.http import JsonResponse
import json
from django.core import serializers
# Create your views here.

def index(request):
    tags = TagInfo.objects.all()
    # 查询最近4章笔记
    notes = NoteInfo.objects.all().order_by('-pub_date')[0: 4]

    return render(request, 'blog/index.html', {'tags':tags, 'notes':notes})

def tag_detail(request, tag_id):
    notes = NoteInfo.objects.filter(tag_id=tag_id)
    show_note = notes[0]
    comments = show_note.commentinfo_set.all().order_by('-id')
    return render(request, 'blog/detail.html', {'show_note': show_note,'notes': notes, 'comments':comments})

def note_detail(request, note_id):
    note = NoteInfo.objects.get(id = note_id)
    content = [note.content]
    comments = []
    for i in note.commentinfo_set.all():
        comments.append(i.content)
    json_data = {'content':content, 'comments':comments}
    return JsonResponse({'json_data': json_data})

def search(request):
    msg = request.GET.get('msg')
    notes = NoteInfo.objects.filter(title__contains=msg)
    note_id = []
    titles = []
    img_urls = []
    tag_names = []
    for i in notes:
        note_id.append(i.id)
        titles.append(i.title)
        img_urls.append(i.tag.img_url)
        tag_names.append(i.tag.name)
    json_data = {'note_id': note_id,'titles':titles, 'img_urls':img_urls, 'tag_names':tag_names}
    # json_data = serializers.serialize('json', objs)
    # json_data = json.loads(json_data)
    return JsonResponse({'json_data': json_data})

def add_comment(request):
    note_id = request.GET.get('note_id');
    comment_content = request.GET.get('comment')
    note = NoteInfo.objects.get(id=note_id)
    comment = CommentInfo()
    comment.content = comment_content
    comment.NoteInfo = note
    comment.save()
    comments = []
    for i in note.commentinfo_set.all():
        comments.append(i.content)
    json_data = {'comments': comments}
    return JsonResponse({'json_data': json_data})

def detail(request, note_id):
    show_note = NoteInfo.objects.get(id=note_id)
    notes = NoteInfo.objects.filter(tag_id=show_note.tag_id)
    comments = show_note.commentinfo_set.all().order_by('-id')
    return render(request, 'blog/detail.html', {'show_note': show_note, 'notes': notes, 'comments': comments})

