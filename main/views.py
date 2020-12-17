from django.shortcuts import render
from django.utils.crypto import get_random_string
from main.forms import UserForm, ReferUserForm

users = []

def homeView(request):
    return render(request, 'main/home.html')

def addUserView(request):
    message = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            user_email = form.cleaned_data['email']
            if any(user['email'] == user_email for user in users):
                message = 'The email address is exists. Please use another email address'
            else:
                users.append({
                    'id': len(users),
                    'email': user_email,
                    'code': get_random_string(6, allowed_chars='ABCDEFG12345'),
                    'referer': '',
                })
        else:
            pass
    form = UserForm()
    return render(request, 'main/add-user.html', {'form': form, 'message': message, 'users': users})

def referUserView(request):
    messages = []
    if request.method == 'POST':
        form = ReferUserForm(request.POST)
        
        if form.is_valid():
            user_email = form.cleaned_data['email']
            referer_code = form.cleaned_data['code']
            refered = {}
            referer = {}
            for user in users:
                if user['email'] == user_email:
                    refered = user
                if user['code'] == referer_code:
                    referer = user
            if refered == referer:
                messages.append('You can not refer yourself')
            elif not refered:
                messages.append('The email address is not exists.')
            elif not referer:
                messages.append("Referer's code is not valid. Please input valid code.")
            elif not refered['referer'] == '':
                messages.append("Someone already refered. Please refer another one.")
            else:
                refered['referer'] = referer['email']
        else:
            pass
    form = ReferUserForm()
    return render(request, 'main/refer-user.html', {'form': form, 'messages': messages})

def countReferalsView(request):
    counter = 0
    user_email = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            for user in users:
                if user['referer'] == user_email:
                    counter += 1
    form = UserForm()
    return render(request, 'main/count-referals.html', {'form': form, 'counter': counter, 'user': user_email})

def getRefererView(request):
    referer = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            referer = next((user['email'] for user in users if user["email"] == user_email), 'No one')
    form = UserForm()
    return render(request, 'main/get-referer.html', {'form': form, 'referer': referer})

def biggestInfluencerView(request):
    try:
        referals = []
        nodes = []
        parents = []
        filtered = []
        buf = []
        referer_emails = set([user['referer'] for user in users])
        for user in users:
            referals.append(0)
            if user['email'] not in referer_emails:
                nodes.append(user)
                referals[user['id']] += 1
        buf = [item for item in users if item not in nodes]
        while 1:
            for node in nodes:
                for arr in buf:
                    print(arr['email'], '==', node['referer'])
                    if arr['email'] == node['referer']:

                        referals[arr['id']] += referals[node['id']]
                        parents.append(arr)
            filtered = [item for item in buf if item not in parents] 
            print(referals)
            if filtered:
                buf = filtered
                nodes = parents
                parents = []
            else:
                break
    except Exception as e:
        print(e)
    return render(request, 'main/biggest-influencer.html')
