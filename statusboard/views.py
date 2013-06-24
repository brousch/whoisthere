from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Status


def index(request):
    all_messages = Status.objects.all()
    
    if request.method == 'POST':
        msg_id = request.POST.get("msg_id", None)
        del_msg = request.POST.get("del_msg", None)
        new_msg = request.POST.get("new_msg", None)
        if (msg_id is not None) and (del_msg is not None):
            try:
                this_status = Status.objects.get(pk=msg_id)
            except:
                error_msg = "Attempted to delete message with invalid message id. Ignoring."
                messages.add_message(request, messages.ERROR, error_msg)
            if this_status:
                try:
                    this_status.delete()
                    success_msg = "Deleted message: {}".format(this_status.msg)
                    messages.add_message(request, messages.SUCCESS, success_msg)
                except:
                    error_msg = "Something went wrong while deleting message {}".format(msg_id)
                    messages.add_message(request, messages.ERROR, error_msg)
        if new_msg is not None:
            try:
                new_status = Status()
                new_status.msg = new_msg
                new_status.save()
                success_msg = "Created new message: {}".format(new_msg)
                messages.add_message(request, messages.SUCCESS, success_msg)
            except:
                error_msg = "Something went wrong while creating: {}".format(new_msg)
                messages.add_message(request, messages.ERROR, error_msg)
    all_msgs = Status.objects.all()
    return render_to_response("status_board.html",
                              {"all_msgs": all_msgs, },
                              context_instance=RequestContext(request))
