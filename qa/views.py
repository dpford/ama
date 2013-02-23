from django import forms

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.context_processors import csrf

from django.template import RequestContext

from django.utils import timezone

from qa.models import Qa
from qa.models import Ama
from qa.models import SearchForm

from django.views.generic import ListView

from django.http import Http404

import json
import urllib2

def index(request):
    if request.method == 'POST': #if form has been submitted
        form = SearchForm(request.POST) #a form bound to the POST data
        if form.is_valid(): #all validation rules pass
            ama_url = form.cleaned_data['amaurl']
            try:
                url = urllib2.urlopen(ama_url+'.json') #add .json to make it a JSON file
            except (ValueError, urllib2.HTTPError):
                raise Http404()
            x = json.load(url)
            url.close()
            orig_poster = x[0]['data']['children'][0]['data']['author']
            title = x[0]['data']['children'][0]['data']['title']
            ama_id = x[0]['data']['children'][0]['data']['id']
            a = Ama(title=title, ama_id=ama_id, orig_poster=orig_poster, created=timezone.now())
            a.save()
            num_main_comment_blocks = len(x[1]['data']['children']) #Number of comment trunks
            for i in range(0,num_main_comment_blocks): #iterate through comment trunks
                if x[1]['data']['children'][i]['data']['replies']: #if there are replies to a comment trunk
                    for p in range(0,len(x[1]['data']['children'][i]['data']['replies']['data']['children'])): #iterate through 1st level replies to comment trunks
                        if x[1]['data']['children'][i]['data']['replies']['data']['children'][p]['data']['author'] == orig_poster: #if author of reply is the OP
                            ama = a
                            asker = x[1]['data']['children'][i]['data']['author'] #person asking the OP a question
                            question = x[1]['data']['children'][i]['data']['body'] #question asked
                            answer = x[1]['data']['children'][i]['data']['replies']['data']['children'][p]['data']['body'] #OP's response
                            ups = x[1]['data']['children'][i]['data']['replies']['data']['children'][p]['data']['ups'] #OP's response's upvotes
                            answered = x[1]['data']['children'][i]['data']['replies']['data']['children'][p]['data']['created_utc']
                            questid = x[1]['data']['children'][i]['data']['id']
                            answerid = x[1]['data']['children'][i]['data']['replies']['data']['children'][p]['data']['id']
                            b = Qa(ama=ama, asker=asker, question=question, answer=answer, ups=ups, answered=answered, questid=questid, answerid=answerid)
                            b.save()
            #run the code, including seeing if it's already in database
            #if not in database, add to database
            #generate page
            return redirect('/'+str(a.id)) #redirect to the new AMA page that is generated
    else:
        form = SearchForm()
    c = {'form': form}
    return render_to_response('home.html', c, context_instance=RequestContext(request))
    
def indexold(request):
    if request.method == "POST":
        url = {}
        url['amaurl'] = (request.POST['url'])
        print request.POST['url']
        return render(request, 'home.html', url)
    return render(request,'home.html', c)
    
class QaListView(ListView):
    def get_queryset(self):
        amaid = self.kwargs['amaid']
        queryset = Qa.objects.filter(ama__id__exact=int(amaid)).order_by('-ups')
        #queryset = Qa.objects.filter(ups__exact=2)
        #queryset = Qa.objects.all()
        return queryset