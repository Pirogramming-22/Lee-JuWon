from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea, IdeaStar, Tool
from .forms import IdeaForm, ToolForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Count
from django.shortcuts import render
from .models import Idea, IdeaStar


# 메인 페이지
def main_page(request):
    sort_by = request.GET.get('sort', '-created_at')  # 기본 정렬 기준은 최신순('-created_at')
    
    # 별점 수를 계산하여 정렬
    if sort_by == '-star_count':
        ideas = Idea.objects.annotate(star_count=Count('ideastar')).order_by('-star_count')  # 별점 수 기준으로 내림차순 정렬
    else:
        ideas = Idea.objects.all().order_by(sort_by)  # 다른 정렬 기준 처리
    
    starred_ideas = []
    
    # 세션 키로 찜한 아이디어 확인
    session_key = request.session.session_key
    if session_key:
        starred_ideas = IdeaStar.objects.filter(session_key=session_key).values_list('idea_id', flat=True)

    return render(request, 'main.html', {'ideas': ideas, 'starred_ideas': list(starred_ideas)})



# 아이디어 추가 페이지
def add_idea(request):
    tools = Tool.objects.all()  # 모든 개발툴 목록을 가져옵니다.
    
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()  # 아이디어를 저장하고 저장된 객체를 `idea`에 할당
            return redirect('idea_detail', idea_id=idea.id)  # 아이디어 디테일 페이지로 리다이렉트
    else:
        form = IdeaForm()
    
    return render(request, 'addIdea.html', {'form': form, 'tools': tools})

# 도구 추가 페이지
def add_tool(request):
    return render(request, 'addTool.html')

# 도구 관리 페이지
def manage_tools(request):
    return render(request, 'manageTools.html')

# 아이디어 상세 페이지
def idea_detail(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    session_key = request.session.session_key  # 세션 키 가져오기
    if session_key:
        is_starred = IdeaStar.objects.filter(session_key=session_key, idea=idea).exists()  # 세션 기준으로 찜 상태 확인
    else:
        is_starred = False
    return render(request, 'ideaDetail.html', {'idea': idea, 'is_starred': is_starred})

# 별 토글 기능
def toggle_star(request, idea_id):
    if request.method == "POST":
        idea = get_object_or_404(Idea, id=idea_id)
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        # 세션 키로 찜 상태를 토글
        star, created = IdeaStar.objects.get_or_create(session_key=session_key, idea=idea)

        if not created:
            star.delete()
            return JsonResponse({"starred": False})
        return JsonResponse({"starred": True})

def delete_idea(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    idea.delete()  # 아이디어 삭제
    return redirect('main_page')  # 메인 페이지로 리다이렉트



# 아이디어 수정 뷰
def update_idea(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    tools = Tool.objects.all()  # 모든 도구를 가져옵니다.

    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        
        if form.is_valid():
            # 이미지가 새로 업로드되지 않았을 경우, 기존 이미지 유지
            if not request.FILES.get('image'):
                form.instance.image = idea.image

            form.save()  # 수정된 내용 저장
            return redirect('idea_detail', idea_id=idea.id)  # 수정된 아이디어 디테일 페이지로 리디렉트
        else:
            print(form.errors)  # 폼 오류 출력
            return render(request, 'ideaDetailUpdate.html', {'form': form, 'idea': idea, 'tools': tools})
    else:
        form = IdeaForm(instance=idea)  # 기존 데이터를 폼에 채움

    return render(request, 'ideaDetailUpdate.html', {'form': form, 'idea': idea, 'tools': tools})





# Tool을 추가하는 뷰
def add_tool(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            tool = form.save()  # 도구 등록
            return redirect('dev_tool_detail', tool_id=tool.id)  # 등록된 도구의 디테일 페이지로 리디렉션
    else:
        form = ToolForm()
    return render(request, 'addTool.html', {'form': form})

# 저장된 Tool 리스트를 보여주는 뷰
def manage_tools(request):
    tools = Tool.objects.all()  # 데이터베이스에서 모든 Tool 객체를 가져옴
    return render(request, 'manageTools.html', {'tools': tools})

# 도구 상세 페이지
def dev_tool_detail(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    return render(request, 'devToolDetail.html', {'tool': tool})

# 도구 삭제
def delete_tool(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    tool.delete()
    return redirect('manage_tools')

# 도구 수정 페이지
def dev_tool_update(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    if request.method == 'POST':
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('dev_tool_detail', tool_id=tool.id)
    else:
        form = ToolForm(instance=tool)
    return render(request, 'devToolUpdate.html', {'form': form, 'tool': tool})


@csrf_exempt
def update_interest(request, idea_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            interest = data.get('interest')

            # 아이디어를 가져와서 관심도 업데이트
            idea = get_object_or_404(Idea, id=idea_id)
            idea.interest = interest
            idea.save()

            return JsonResponse({"success": True, "interest": interest})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request method"})